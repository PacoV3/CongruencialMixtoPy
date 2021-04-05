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
    prev_inspection_end_a = 0
    prev_inspection_end_b = 0
    for piece in range(n_pieces):
        # Random values
        r, u1, u2 = get_n_rands(3)
        exp_t = dist_exponential(l, r)
        norm_t = dist_normal(u1, u2, mean, sd)
        # Arrival vals
        arrival = prev_arrival + exp_t
        if not prev_arrival:
            inspection_start_a = arrival
            inspection_start_b = 0
            prev_inspection_end_a = inspection_start_a + norm_t
            prev_inspection_end_b = 0
        else:
            inspection_start_a = arrival if prev_inspection_end_a > prev_inspection_end_b else min(prev_inspection_end_a, prev_inspection_end_b)
            inspection_start_b = arrival if prev_inspection_end_a < prev_inspection_end_b else min(prev_inspection_end_a, prev_inspection_end_b)
            prev_inspection_end_a = prev_inspection_end_a if inspection_start_a == 0 else inspection_start_a + norm_t
            prev_inspection_end_b = prev_inspection_end_b if inspection_start_b == 0 else inspection_start_b + norm_t
        prev_arrival = arrival
        # Inspection vals
        inspection_times.append(max(inspection_start_a, inspection_start_b) + norm_t - arrival)
    return inspection_times


pieces = 5000
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
plt.savefig("graphs/two_servers.png")
