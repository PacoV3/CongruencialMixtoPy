from ast import literal_eval as make_tuple
from new_line_txt import write_line_txt
from var_generator import generate_values
from mean_test import check_mean_test


def select_next_variables(file_name):
    with open(file_name+'.txt') as f:
        line = f.readline().replace('\n', '')
    return make_tuple(line)


def cal_xn1(a, c, m, Xn):
    # Retorna el cálculo de Xn + 1 a partir de a, c, m y Xn
    return (a*Xn+c) % m


def rand_mix(reset_vars=False):
    if reset_vars:
        generate_values(1, 'variables')
        del rand_mix.count
        return
    # Si no existe la cuenta es igual a 0 y busca las siguientes variables y actualiza
    if not hasattr(rand_mix, 'count'):
        rand_mix.count = 0
        rand_mix.a, rand_mix.c, rand_mix.m, rand_mix.Xn = select_next_variables(
            'variables')
    # Calcula Xn + 1 a partir de las variables y Xn
    Xn1 = cal_xn1(rand_mix.a, rand_mix.c, rand_mix.m, rand_mix.Xn)
    # Almacena Xn + 1 como el nuevo Xn
    rand_mix.Xn = Xn1
    # Aumentar la cantidad de veces que se ha ejecutado rand_mix()
    rand_mix.count += 1
    # Si la cuenta es igual a m -> borra para generar nuevos números
    if rand_mix.count == rand_mix.m:
        # Si la cuenta de lineas es igual a el total de lineas -> borra para generar nuevas variables
        generate_values(1, 'variables')
        del rand_mix.count
    # Regresa la variable dividiendo Xn + 1 entre m
    return Xn1 / rand_mix.m

def use_mean_test(times, sample_size):
    pseudo = []
    correct_variables = 0
    for turn in range((times + 1) * sample_size):
        if turn % sample_size == 0 and turn != 0:
            a, c, m, seed = select_next_variables('variables')
            if check_mean_test(pseudo):
                correct_variables += 1
                write_line_txt(a, c, m, seed,'mean_variables')
            else:
                print('Error in: ' + str((a, c, m, seed)))
            pseudo = []
            rand_mix(reset_vars=True)
        pseudo.append(rand_mix())
    return correct_variables / times, times - correct_variables

acc, errors = use_mean_test(100,200)
print(f"\nErrors: {errors}, Accuracy: {acc}")