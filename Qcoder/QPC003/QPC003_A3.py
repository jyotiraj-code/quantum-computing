import math
from qiskit import QuantumCircuit

def solve() -> QuantumCircuit:
    qc = QuantumCircuit(3)

    # Define rotation angles for controlled-Ry gates
    theta1 = 2 * math.atan(math.sqrt(2))  # Angle to create superposition on first target
    theta2 = 2 * math.atan(1)              # Angle to balance amplitudes between states

    # Start with the initial state by flipping qubit 0
    qc.x(0)

    # Apply controlled-Ry rotation with qubit 0 as control and qubit 1 as target
    qc.cry(theta1, 0, 1)
    
    # Apply CNOT with qubit 1 as control and qubit 0 as target to entangle states
    qc.cx(1, 0)
    
    # Apply controlled-Ry with qubit 1 as control and qubit 2 as target
    qc.cry(theta2, 1, 2)
    
    # Apply CNOT with qubit 2 as control and qubit 1 as target
    qc.cx(2, 1)

    return qc
