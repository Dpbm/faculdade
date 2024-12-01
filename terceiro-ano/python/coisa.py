from micromoth import QuantumCircuit, simulate

qc = QuantumCircuit(2,2)
qc.x(0)
#qc.swap(0,1)
qc.measure(0,0)
qc.measure(1,1)
print(simulate(qc,shots=1000,get='counts'))

