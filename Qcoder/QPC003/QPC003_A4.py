import math
 
from qiskit import QuantumCircuit
 
 
def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
 
    theta = [2 * math.atan(math.sqrt(i)) for i in range(n - 1, 0, -1)]
 
    qc.x(0)
 
    for i in range(n - 1):
        qc.cry(theta[i], i, i + 1)
        qc.cx(i + 1, i)
 
    return qc
