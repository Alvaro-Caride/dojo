from mpi4py import MPI
import numpy as np

from qulacs import QuantumState
from qulacs.gate import X, RY, DenseMatrix, merge

comm = MPI.COMM_WORLD

n = 3
state = QuantumState(n)
state.set_zero_state()
print(state.get_vector())

# X operation on 1st-qubit (|000> -> |010>)
index = 1
x_gate = X(index)
x_gate.update_quantum_state(state)
print(state.get_vector())

# pi/4.0 rotation on 1st-qubit with Y-pauli
angle = np.pi / 4.0
ry_gate = RY(index, angle)
ry_gate.update_quantum_state(state)
print(state.get_vector())

# Apply gate created by gate matrix to 2nd-qubit
dense_gate = DenseMatrix(2, [[0,1],[1,0]])
dense_gate.update_quantum_state(state)
print(state.get_vector())

# Release gates
del x_gate
del ry_gate
del dense_gate

"""
Avaliable GATES

    - single-qubit Pauli operation: Identity, X, Y, Z

    - single-qubit Clifford operation : H, S, Sdag, T, Tdag, sqrtX, sqrtXdag, sqrtY, sqrtYdag

    - two-qubit Clifford operation : CNOT, CZ, SWAP

    - single-qubit Pauli rotation : RX, RY, RZ

    - General Pauli operation : Pauli, PauliRotation

    - IBMQ basis-gate : U1, U2, U3

    - General gate : DenseMatrix

    - Measurement : Measurement

    - Noise : BitFlipNoise, DephasingNoise, IndepenedentXZNoise, DepolarizingNoise

"""


print(" ")
print("Merged Gate")

n = 3
state = QuantumState(n)
state.set_zero_state()

index = 1
x_gate = X(index)
angle = np.pi / 4.0
ry_gate = RY(index, angle)

# Synthesize gates to create a new gate
# First argument acts first
x_and_ry_gate = merge(x_gate, ry_gate)
x_and_ry_gate.update_quantum_state(state)
print(state.get_vector())








