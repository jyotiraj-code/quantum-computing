from qiskit import QuantumCircuit


def solve(n: int, L: int, theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in range(n):
        if not (1<<i) & L:
            qc.x(i)
    if n == 1:
        qc.p(theta, n-1)
    else:
        qc.mcp(theta, list(range(n - 1)), n - 1)
    for i in range(n):

        if not(1<<i) & L:
            qc.x(i) 

    return qc
