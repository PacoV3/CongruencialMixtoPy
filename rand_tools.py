from math import log, exp, factorial, sqrt, cos, pi


def dist_normal(u1, u2, mean, sd):
    '''
    Funcion para obtener un valor aleatorio en la distribucion
    normal en base a una media y una desviacion estandar
    '''
    x = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
    return x * sd + mean


def dist_uniform(a, b, R):
    '''
    Funcion para obtener un valor uniforme en el rango de 
    "a" a "b" 
    '''
    return a + (b - a) * R


def dist_exponential(l, R):
    return -l * log(1 - R)


def dist_bernoulli(p, R):
    if R >= (1 - p):
        return 1
    return 0


def dis_poisson(l, R):
    def px(l, x): return l**x * exp(-l) / factorial(x)
    x = 0
    izq = 0
    der = px(l, x)
    while True:
        if izq <= R < der:
            return x
        x += 1
        izq = der
        der = der + px(l, x)


def dist_erlang(l, list_R):
    k = len(list_R)
    x = 1
    for rand in list_R:
        x = x * (1 - rand)
    return -1 / (k * l) * log(x)


# list_of_pair_rands = [ (R0,R1), (R0,R1), (R0,R1) ]
def pi_montecarlo(list_of_pair_rands):
    n = len(list_of_pair_rands)
    n_inside_circle = 0
    for r0, r1 in list_of_pair_rands:
        x = dist_uniform(-1, 1, r0)
        y = dist_uniform(-1, 1, r1)
        d = x**2 + y**2
        if d < 1:
            n_inside_circle += 1
    return n_inside_circle / n * 4


if __name__ == "__main__":
    pass
