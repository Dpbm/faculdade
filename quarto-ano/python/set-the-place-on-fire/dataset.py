from qiskit.circuit.random import random_circuit
from qiskit import qasm3
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel
from qiskit_aer.primitives import Sampler
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeAthensV2, FakeBelemV2, FakeCasablancaV2
import matplotlib.pyplot as plt
import numpy as np
import os
from multiprocessing.pool import Pool
from tqdm import tqdm
import pandas as pd
import json

SHOTS = 1000
MIN_DEPTH = 1
MAX_DEPTH = 4
TOTAL_THREADS = 5
DATASET_SIZE = 1000
BACKENDS = [FakeAthensV2, FakeBelemV2, FakeCasablancaV2]
DATASET_PATH = os.path.join('.', 'dataset')

def generate(backend, sim, index):
    n_qubits = backend.num_qubits
    depth = np.random.randint(MIN_DEPTH, MAX_DEPTH)
    qc = random_circuit(n_qubits, depth)
    qc.measure_all()

    filename = f"{n_qubits}-{index}.qasm" 
    qasm_file_path = os.path.join(DATASET_PATH, filename)

    with open(qasm_file_path, "w", encoding="utf-8") as qasm_file:
        qasm3.dump(qc, qasm_file)

    pm_aer = generate_preset_pass_manager(backend=sim, optimization_level=0)
    aer_isa = pm_aer.run([qc])[0]

    # aer_isa.draw('mpl')
    # plt.show()

    sampler_aer = Sampler()
    result_aer = sampler_aer.run([aer_isa], shots=SHOTS).result().quasi_dists[0]
    
    pm_backend = generate_preset_pass_manager(backend=backend, optimization_level=0)
    backend_isa = pm_backend.run([qc])[0]

    noise_model = NoiseModel.from_backend(backend)
    sampler_aer_noise = Sampler(
         run_options={
            "noise_model": noise_model,
            "coupling_map": backend.configuration().coupling_map,
            "basis_gates": noise_model.basis_gates,
        }
    )
    result_backend = sampler_aer_noise.run([backend_isa], shots=SHOTS).result().quasi_dists[0]

    return {
        "n_qubits":n_qubits,
        "depth":depth,
        "backend":backend.name,
        "file": filename,
        "aer_result": json.dumps(result_aer),
        "backend_result": json.dumps(result_backend)
    }
    
def main():
    os.makedirs(DATASET_PATH, exist_ok=True)

    index = 0 
    df = pd.DataFrame(columns=("n_qubits","depth", "backend", "file", "aer_result", "backend_result"))

    with tqdm(total=DATASET_SIZE)  as progress:

        while index < DATASET_SIZE:
            args = []
            for i in range(TOTAL_THREADS):
                selected_backend = np.random.choice(BACKENDS)
                sim = AerSimulator()
                args.append((selected_backend(), sim, index))
                index += 1

            with Pool(processes=TOTAL_THREADS) as pool:
                results = pool.starmap(generate, args)
            
            for result in results:
                df.loc[len(df)] = result

            progress.update(TOTAL_THREADS)

    df.to_csv("dataset.csv", index=False)

if __name__ == "__main__":
    main()