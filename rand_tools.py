def uniform(a, b, R):
    return a + (b - a) * R


# list_of_pair_rands = [ (R0,R1), (R0,R1), (R0,R1) ]
def pi_montecarlo(list_of_pair_rands):
    n = len(list_of_pair_rands)
    n_inside_circle = 0
    for r0, r1 in list_of_pair_rands:
        x = uniform(-1, 1, r0)
        y = uniform(-1, 1, r1)
        d = x ** 2 + y ** 2
        if d < 1:
            n_inside_circle += 1
    return n_inside_circle / n * 4
