from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.cx(0,1)
    qc.cx(1,0)
    qc.cx(0,1)

    return qc