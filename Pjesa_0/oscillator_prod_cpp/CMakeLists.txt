cmake_minimum_required(VERSION 3.16)
project(oscillator_prod_demo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(oscillator
    src/main.cpp
    src/integrators.cpp
    src/oscillator.cpp
    src/cli.cpp
)

target_include_directories(oscillator PRIVATE include)
