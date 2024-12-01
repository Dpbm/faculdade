require "MicroMoth"

local qc = QuantumCircuit()
qc.set_registers(2,2)
qc.x(0)
qc.swap(0,1)
--qc.cx(0,1)
qc.measure(0,0)
qc.measure(1,1)
--print(qc)

result = simulate(qc,"counts",10)

--print this to screen
--print("\nThe counts are\n")
for string, counts in pairs(result) do
  print("Counts for",string,"=",counts)
end
