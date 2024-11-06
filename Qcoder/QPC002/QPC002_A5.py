from qiskit import QuantumCircuit
import math


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    qc.h(0)
    for i in range(int(math.log2(n))+1):
        for j in range(2**i):
            if 2**i + j == n:
                break
            qc.cx(j,2**i+j)
    qc.z(0)

    return qc
