use pyo3::prelude::*;
use pyo3::types::*;
use std::collections::HashMap;

fn main() -> PyResult<()> {
    pyo3::prepare_freethreaded_python();

    let qasm_data = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/test.qasm"));

    Python::with_gil(|py| {
        let parse = PyModule::import_bound(py, "openqasm3")?.getattr("parse")?;
        let result: Py<PyAny> = parse.call1((qasm_data,))?.into();
        let data: PyAny = result.extract()?;
        println!("{}", data.hasattr("version"));
        Ok(())
    })
}
