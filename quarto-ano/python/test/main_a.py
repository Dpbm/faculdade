from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime.fake_provider import FakeBelemV2
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from tqdm import trange
import numpy as np
from scipy.optimize import minimize 

qc = QuantumCircuit(2)
qc.h(range(2))

a,b = Parameter('a'), Parameter('b')

qc.ry(a,0)
qc.ry(b,1)


samples = 100
expected = 2.0

error = 1
goal = 0.0001

obs = SparsePauliOp(["IX", "XI"])
backend = FakeBelemV2()
estimator = Estimator(backend)
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)

isa = pm.run(qc)
isa_obs = obs.apply_layout(isa.layout)

params = np.array([np.pi, np.pi])


def obj(params):
    results = np.zeros(samples)
    for sample in trange(samples):
        exp = estimator.run([(isa,isa_obs,[params])]).result()[0].data.evs[0]
        results[sample] = exp

    error = (expected-results).mean()
    print(f"error: {error}; params: {params}")
    return error

result = minimize(obj, x0=params, method="BFGS")

with open("params.npy", "w") as file:
    np.save(file, result.x)




