from qiskit import QuantumCircuit
import math


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in reversed(range(n)):
        qc.h(i)
        for j in reversed(range(i)):
            qc.cp(math.pi/2**(i-j),j,i)
    for i in range(n//2):
        qc.swap(i, n-i-1)

    return qc
