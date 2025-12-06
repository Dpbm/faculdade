#!/usr/bin/env bash

c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) ran.cpp -o ran$(python3 -m pybind11 --extension-suffix)
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) rand.cpp -o rand$(python3 -m pybind11 --extension-suffix)
