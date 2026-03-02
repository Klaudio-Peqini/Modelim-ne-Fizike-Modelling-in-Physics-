module OscillatorProdDemo

export OscillatorParams, rhs, energy, simulate_euler, simulate_rk4, simulate_verlet

struct OscillatorParams
    omega::Float64
end

# state = (x, v)
rhs(s::NTuple{2,Float64}, p::OscillatorParams) = (s[2], -(p.omega^2)*s[1])
energy(s::NTuple{2,Float64}, p::OscillatorParams) = 0.5*s[2]^2 + 0.5*(p.omega^2)*s[1]^2

function simulate_euler(s0::NTuple{2,Float64}, p::OscillatorParams, t_end::Float64, dt::Float64)
    N = Int(floor(t_end/dt)) + 1
    t = collect(0.0:dt:(dt*(N-1)))
    y = Vector{NTuple{2,Float64}}(undef, N)
    y[1] = s0
    for n in 1:(N-1)
        k1 = rhs(y[n], p)
        y[n+1] = (y[n][1] + dt*k1[1], y[n][2] + dt*k1[2])
    end
    return t, y
end

function simulate_rk4(s0::NTuple{2,Float64}, p::OscillatorParams, t_end::Float64, dt::Float64)
    N = Int(floor(t_end/dt)) + 1
    t = collect(0.0:dt:(dt*(N-1)))
    y = Vector{NTuple{2,Float64}}(undef, N)
    y[1] = s0
    for n in 1:(N-1)
        s = y[n]
        k1 = rhs(s, p)
        k2 = rhs((s[1] + 0.5*dt*k1[1], s[2] + 0.5*dt*k1[2]), p)
        k3 = rhs((s[1] + 0.5*dt*k2[1], s[2] + 0.5*dt*k2[2]), p)
        k4 = rhs((s[1] + dt*k3[1], s[2] + dt*k3[2]), p)
        y[n+1] = (
            s[1] + (dt/6.0)*(k1[1] + 2k2[1] + 2k3[1] + k4[1]),
            s[2] + (dt/6.0)*(k1[2] + 2k2[2] + 2k3[2] + k4[2])
        )
    end
    return t, y
end

function simulate_verlet(s0::NTuple{2,Float64}, p::OscillatorParams, t_end::Float64, dt::Float64)
    N = Int(floor(t_end/dt)) + 1
    t = collect(0.0:dt:(dt*(N-1)))
    y = Vector{NTuple{2,Float64}}(undef, N)
    y[1] = s0
    x, v = s0
    for n in 1:(N-1)
        a = -(p.omega^2)*x
        x_new = x + v*dt + 0.5*a*dt^2
        a_new = -(p.omega^2)*x_new
        v_new = v + 0.5*(a + a_new)*dt
        x, v = x_new, v_new
        y[n+1] = (x, v)
    end
    return t, y
end

end # module
