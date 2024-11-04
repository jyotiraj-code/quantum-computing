#Less than a Oracle

from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate

def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for l in range(L):
        for i in range(n):
            #Checking if the ith bit is 0 or 1
            if not (l>>i & 1):
                qc.x(i)
        #Applying the Z rotation
        if n==1:
            qc.z(0)
        else:
            qc.append(ZGate().control(n-1), range(n))

        for i in range(n):
            #Doing the inverse of the step 1
            if not (l>>i & 1):
                qc.x(i)

    return qc

