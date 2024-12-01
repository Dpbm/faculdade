use pyo3::prelude::*;

fn main() -> PyResult<()> {
    pyo3::prepare_freethreaded_python();
    Python::with_gil(|py| {
        let py_app = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/test_py/test.py"));
        let func_data = PyModule::from_code_bound(py, py_app, "test.py", "test")?;
        let func: Py<PyAny> = func_data.getattr("testt")?.into();
        func.call0(py);
        Ok(())
    })
}