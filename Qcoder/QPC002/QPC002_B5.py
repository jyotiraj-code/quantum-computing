from qiskit import QuantumCircuit
import math

def solve(n: int, m: int, S: list[int]) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in range(n):
        theta = 2*math.pi*S[i]/2**m
        qc.p(theta,i)

    return qc
