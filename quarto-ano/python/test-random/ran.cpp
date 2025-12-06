#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i, int j){
	return i+j;
}

PYBIND11_MODULE(ran, m, py::mod_gil_not_used()){
	m.def("add", &add, "whatever");
}
