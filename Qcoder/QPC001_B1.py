#Copy Oracle

from qiskit import QuantumCircuit, QuantumRegister


def solve() -> QuantumCircuit:
    x, y = QuantumRegister(1), QuantumRegister(1)
    qc = QuantumCircuit(x, y)
    qc.cx(x,y)
    # Write your code here:

    return qc
