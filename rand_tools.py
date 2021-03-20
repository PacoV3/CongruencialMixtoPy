from math import log, exp, factorial


def dist_uniform(a, b, R):
    return a + (b - a) * R


def dist_exponential(l, R):
    return -1 / l * log(R)


def dist_bernoulli(p, R):
    if R >= (1 - p):
        return 1
    return 0


def dis_poisson(l, R):
    px = lambda l, x : l ** x * exp(-l) / factorial(x)
    x = 0
    izq = 0
    der = px(l, x)
    while True:
        if izq <= R < der:
            return x
        x += 1
        izq = der
        der = der + px(l, x)


# list_of_pair_rands = [ (R0,R1), (R0,R1), (R0,R1) ]
def pi_montecarlo(list_of_pair_rands):
    n = len(list_of_pair_rands)
    n_inside_circle = 0
    for r0, r1 in list_of_pair_rands:
        x = dist_uniform(-1, 1, r0)
        y = dist_uniform(-1, 1, r1)
        d = x ** 2 + y ** 2
        if d < 1:
            n_inside_circle += 1
    return n_inside_circle / n * 4


if __name__ == "__main__":
    print(dis_poisson(5, 0.85))
    print(dis_poisson(7, 0.85))
