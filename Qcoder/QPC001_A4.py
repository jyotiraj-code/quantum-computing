#Generate the state 1/sqrt(3) (|00> + |01> + |10>)

from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.h(0)
    qc.ch(0,1)
    qc.cx(1,0)
    return qc
