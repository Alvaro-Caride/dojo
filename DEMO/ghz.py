from qulacs import QuantumState, QuantumCircuit
from qulacs.circuit import QuantumCircuitOptimizer

import numpy as np
from mpi4py import MPI
"""
Inicialización MPI

"""
mpicomm = MPI.COMM_WORLD
mpirank = mpicomm.Get_rank()
mpisize = mpicomm.Get_size()
# Solo por información. La división interna la hace igual
globalqubits = int(np.log2(mpisize))

qubits =
state = QuantumState(qubits, <Placeholder>)
state.set_zero_state()

circuit = QuantumCircuit(qubits)
circuit.add_H_gate(0)
for i in range(1, qubits):
    circuit.add_CNOT_gate(0, i)

# Optimize?
opt = <Placeholder>
opt.<Placeholder>

# Update
<Placeholder>

# Para que en el print no haya code replication
if mpirank == 0:
    print(state.get_vector())

# imprimir información sobre la ejecución
if mpirank == 0:
    devicename = state.get_device_name()
    print("Device name of the state vector:", devicename)
    if devicename == "multi-cpu":
        print("- Number of qubits:", nqubits)
        print("- Number of global qubits:", globalqubits)
        print("- Number of local qubits:", nqubits - globalqubits)
