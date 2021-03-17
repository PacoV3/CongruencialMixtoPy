def uniform(a, b, R):
    return a + (b - a) * R


# list_of_pair_rands = [ (R0,R1), (R0,R1), (R0,R1) ]
def pi_montecarlo(list_of_pair_rands):
    n = len(list_of_pair_rands)
    
