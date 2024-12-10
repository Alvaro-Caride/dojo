from mpi4py import MPI

import numpy as np
from qulacs import QuantumState
from qulacs.gate import P0,P1,add, merge, Identity, X, Z

comm = MPI.COMM_WORLD

gate00 = merge(P0(0),P0(1))
gate11 = merge(P1(0),P1(1))
# |00><00| + |11><11|
proj_00_or_11 = add(gate00, gate11)
print(proj_00_or_11)

gate_ii_zz = add(Identity(0), merge(Z(0),Z(1)))
gate_ii_xx = add(Identity(0), merge(X(0),X(1)))
proj_00_plus_11 = merge(gate_ii_zz, gate_ii_xx)
# ((|00>+|11>)(<00|+<11|))/2 = (II + ZZ)(II + XX)/4
proj_00_plus_11.multiply_scalar(0.25)
print(proj_00_plus_11)
