#include <pybind11/pybind11.h>
#include <random>

namespace py = pybind11;

int cpp_seed(){
	return std::random_device()();
}

PYBIND11_MODULE(rand, m, py::mod_gil_not_used()){
	m.def("cpp_seed", &cpp_seed, "get seed from random device");
}
