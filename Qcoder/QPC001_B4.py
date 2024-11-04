#Less than a Oracle 2

from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in range(n):
        if not (L >> i) & 1:
            continue
        for j in range(i+1,n):
            if not (L>>j) & 1:
                qc.x(j)
        qc.x(i)
        if i== n-1:
            qc.z(i)
        else:
            qc.append(ZGate().control(n-i-1), range(i,n))
        qc.x(i)
        for j in range(i+1,n):
            if not (L>>j) & 1:
                qc.x(j)



    return qc

