def select_next_variables():
    if not hasattr(select_next_variables, 'count'):
        select_next_variables.count = 0
    # m_values = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
    #             193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]
    # coprimes = [(13, 14),(28, 57),(1, 99),(2, 97),(46, 67),(75, 41)]
    select_next_variables.count += 1
    return {'a': 5, 'c': 7, 'm': 8 * select_next_variables.count, 'seed': 4 + select_next_variables.count - 1}


def cal_xn1(a, c, m, Xn):
    # Retorna el cálculo de Xn + 1 a partir de a, c, m y Xn
    return (a*Xn+c) % m


def rand_mix():
    # Si no existe la cuenta es igual a 0
    if not hasattr(rand_mix, 'count'):
        rand_mix.count = 0
    # Si es igual a 0 busca las siguientes variables y actualiza
    if rand_mix.count == 0:
        cal_vars = select_next_variables()
        rand_mix.a = cal_vars['a']
        rand_mix.c = cal_vars['c']
        rand_mix.m = cal_vars['m']
        rand_mix.Xn = cal_vars['seed']
    # Calcula Xn + 1 a partir de las variables y Xn
    Xn1 = cal_xn1(rand_mix.a, rand_mix.c, rand_mix.m, rand_mix.Xn)
    # Aumentar la cantidad de veces que se ha ejecutado rand_mix()
    rand_mix.count += 1
    # Si la cuenta es igual a m -> borra para generar nuevos números
    if rand_mix.count == rand_mix.m:
        del rand_mix.count
    # Almacena Xn + 1 como el nuevo Xn
    rand_mix.Xn = Xn1
    # Regresa la variable dividiendo Xn + 1 entre m
    return Xn1 / rand_mix.m


for m in range(24):
    if m % 8 == 0:
        print()
    print(rand_mix())
