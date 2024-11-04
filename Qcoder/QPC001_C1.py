#Generate Uniform Amplitude Superposition State I

from qiskit import QuantumCircuit
import math


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    if L == 1:
        return qc
    k = math.ceil(math.log2(L))
    qc.h(range(k))

    return qc
