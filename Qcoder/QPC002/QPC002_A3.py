from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    qc.h(0)
    for i in range(n):
        if i==0:
            continue
        else:
            qc.cx(0,i)

    qc.z(0)

    return qc
