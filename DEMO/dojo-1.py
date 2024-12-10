from mpi4py import MPI
from qulacs import QuantumState

from qulacs.state import inner_product

def main():
	# MPI initialiization	
	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()
	#######################
	# State operations
	n = 5
	state = QuantumState(n)

	#Zero State
	state.set_zero_state()
	print(state.get_vector())
	
	#inizialize to |00101>
	state.set_computational_basis(0b00101)
	print(state.get_vector())
	
	# Random State	
	state.set_Haar_random_state()
	print(state.get_vector())

	# Copy and load Data
	second_state = state.copy()
	print(second_state.get_vector())

	third_state = QuantumState(n)
	third_state.load(state)
	print(third_state.get_vector())	
	####################################
	# Deleting states to give back memory
	del second_state
	del third_state
	####################################
	# Other State Operations
	state = QuantumState(n)
	state.set_Haar_random_state()

	# Calculation of norm (renamed from get_norm to get_squared_norm in qulacs v0.1.8)
	norm = state.get_squared_norm()
	print("squared_norm : ", norm)

	# compute entropy when measured in Z basis
	entropy = state.get_entropy()
	print("entropy : ",entropy)

	# Calculate the probability of getting 0 when measuring index-th qubit in Z basis
	index = 3
	zero_probability = state.get_zero_probability(index)
	print("prob_meas_3rd : ",zero_probability)

	# Calculation of the marginal probability (below is an example of the probability that 0,3-th qubit is measured as 0 and 1,2-th qubit is measured as 1)
	value_list = [0,1,1,0,2]
	marginal_probability = state.get_marginal_probability(value_list)
	print("marginal_prob : ",marginal_probability)

	######################################
	# Inner Product
	state_bra = QuantumState(n)
	state_ket = QuantumState(n)
	state_bra.set_Haar_random_state()
	state_ket.set_computational_basis(0)

	value = inner_product(state_bra, state_ket)
	print(value)

	#######################################
	# Detailed state information
	
	print("Haar random")
	print(state_bra)

	# Finalize MPI. Could be avoided
	MPI.Finalize()

if __name__ == "__main__":
	main()
