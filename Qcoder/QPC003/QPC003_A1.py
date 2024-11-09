from qiskit import QuantumCircuit
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    theta = math.pi/2
    qc.x(0)
    qc.p(theta, 0)

    return qc
