def select_next_variables():
    # select_next_variables.seed = 0
    # m_values = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
    #             193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]
    # coprimes = [(13, 14),(28, 57),(1, 99),(2, 97),(46, 67),(75, 41)]
    return {'a':5,'c':7,'m':8,'seed':4}

def cal_xn1(a, c, m, Xn):
    return (a*Xn+c) % m

def rand_mix():
    cal_vars = select_next_variables()
    if not hasattr(rand_mix,'Xn'):
        rand_mix.Xn = cal_vars['seed']
    Xn1 = cal_xn1(cal_vars['a'],cal_vars['c'],cal_vars['m'],rand_mix.Xn)
    rand_mix.Xn = Xn1
    return Xn1 / cal_vars['m']

for m in range(20):
    if m % 8 == 0:
        print()
    print(rand_mix())
