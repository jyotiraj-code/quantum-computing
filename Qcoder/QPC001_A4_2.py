#Generate the state 1/sqrt(3) (|00> + |01> + |10>) (with the global phase)

from qiskit import QuantumCircuit
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    angle = 2*math.atan(math.sqrt(2))
    qc.ry(angle,0)
    qc.ch(0,1)
    qc.cx(1,0)

    return qc
