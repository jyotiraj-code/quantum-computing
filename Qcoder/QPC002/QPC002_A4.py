from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
 
    qc.h(0)
    qc.cx(0, 1)
 
    for i in range(2, n - 1, 2):
        qc.cx(0, i)
        qc.cx(1, i + 1)
 
    if n % 2 != 0:
        qc.cx(0, n - 1)
 
    qc.z(0)
 
    return qc
