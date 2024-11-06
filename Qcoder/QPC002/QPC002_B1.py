from qiskit import QuantumCircuit


def solve(theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.x(0)
    qc.p(theta,0)
    qc.x(0)

    return qc
