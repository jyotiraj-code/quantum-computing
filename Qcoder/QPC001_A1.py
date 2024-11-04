#Generate the plus state

from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.h(0)

    return qc
