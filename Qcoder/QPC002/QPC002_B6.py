import math
 
from qiskit import QuantumCircuit, QuantumRegister
 
 
def qft(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
 
    for i in reversed(range(n)):
        qc.h(i)
        for j in reversed(range(i)):
            qc.cp(math.pi / 2 ** (i - j), j, i)
 
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
 
    return qc
 
 
def solve(n: int, m: int, S: list[int]) -> QuantumCircuit:
    x, y = QuantumRegister(n), QuantumRegister(m)
    qc = QuantumCircuit(x, y)
 
    qc.h(y)
 
    for j in range(m):
        for i in range(n):
            theta = (2 * math.pi * S[i] / 2**m) * 2**j
            qc.cp(theta, x[i], y[j])
 
    qc.compose(qft(m).inverse(), y, inplace=True)
 
    return qc