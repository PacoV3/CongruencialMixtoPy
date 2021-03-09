from linecache import getline
from json import loads
from var_generator import generate_values
from mean_test import check_mean_test


def select_next_variables(file_name, position):
    line = getline(file_name+'.txt', position).replace("'",'"').replace('\n', '')
    variables = loads(line)
    return {'a': variables['a'], 'c': variables['c'], 'm': variables['m'], 'seed': variables['seed']}


def cal_xn1(a, c, m, Xn):
    # Retorna el cálculo de Xn + 1 a partir de a, c, m y Xn
    return (a*Xn+c) % m


def rand_mix():
    # Contador de linea en variables
    if not hasattr(rand_mix, 'line_count'):
        rand_mix.line_count = 1
    # Si no existe la cuenta es igual a 0
    if not hasattr(rand_mix, 'count'):
        rand_mix.count = 0
    # Si es igual a 0 busca las siguientes variables y actualiza
    if rand_mix.count == 0:
        cal_vars = select_next_variables('variables', rand_mix.line_count)
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
        # Si la cuenta de lineas es igual a el total de lineas -> borra para generar nuevas variables
        if rand_mix.line_count == len(open('variables.txt').readlines()):
            generate_values(50, 'variables')
            del rand_mix.line_count
        else:
            rand_mix.line_count += 1
        del rand_mix.count
    # Almacena Xn + 1 como el nuevo Xn
    rand_mix.Xn = Xn1
    # Regresa la variable dividiendo Xn + 1 entre m
    return Xn1 / rand_mix.m

pseudo_100 = []
for m in range(100):
    pseudo_100.append(rand_mix())

check_mean_test(pseudo_100)

# Por si se quiere refrescar la lista
# generate_values(500, 'variables')
