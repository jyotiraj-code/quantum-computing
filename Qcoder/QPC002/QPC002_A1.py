from qiskit import QuantumCircuit
from math import pi


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.x(0)
    qc.z(0)
    qc.x(0)

    return qc
