import numpy as np
from rand_tools import dist_exponential, dist_normal
import matplotlib.pyplot as plt
from mixto import rand_mix


def get_n_rands(n):
	rands = []
	for _ in range(n):
		rands.append(rand_mix(from_txt="txts/poker_variables"))
	return tuple(rands)


def run_simulation(n_pieces, l, mean, sd):
	"""
	Funcion para simular una linea de produccion a partir de una cantidad
	de piezas
	"""
	inspection_times = []
	prev_arrival = 0
	prev_inspection_end = 0
	for piece in range(n_pieces):
		# Random values
		r, u1, u2 = get_n_rands(3)
		exp_t = dist_exponential(l, r)
		norm_t = dist_normal(u1, u2, mean, sd)
		# Arrival vals
		arrival = prev_arrival + exp_t
		prev_arrival = arrival
		# Inspection vals
		inspection_start = max(arrival, prev_inspection_end)
		inspection_end = inspection_start + norm_t
		inspection_times.append(inspection_end - arrival)
		prev_inspection_end = inspection_end
	return inspection_times


pieces = 2000
ins_times = run_simulation(pieces, l=5, mean=4, sd=0.5)

x = range(len(ins_times))
# Get averages
y = [np.mean(ins_times[:piece + 1]) for piece in range(len(ins_times))]
# Graph
plt.title("Simulation behavior")
plt.xlabel("Piece number")
plt.ylabel("Average time in inspection")
plt.plot(x, y, color="red")
plt.legend([f"servers = {1}, pieces = {pieces}"], loc="upper right")
plt.savefig("graphs/one_server.png")
