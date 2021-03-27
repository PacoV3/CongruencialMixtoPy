import numpy as np
from ast import literal_eval as make_tuple
from new_line_txt import write_line_txt
from var_generator import generate_variables
from test import check_mean_test, check_frequency_test, check_series_test, check_poker_test
from rand_tools import dist_uniform, pi_montecarlo


def select_next_variables(file_name):
    with open(file_name + '.txt') as f:
        line = f.readline().replace('\n', '')
    return make_tuple(line)


def cal_xn1(a, c, m, Xn):
    # Retorna el cálculo de Xn + 1 a partir de a, c, m y Xn
    return (a * Xn + c) % m


def rand_mix(reset_vars=False, from_txt='txts/poker_variables', vars=None):
    if reset_vars:
        del rand_mix.count
        return
    # Si no existe la cuenta es igual a 0 y busca las siguientes variables y actualiza
    if not hasattr(rand_mix, 'count'):
        rand_mix.count = 0
        rand_mix.a, rand_mix.c, rand_mix.m, rand_mix.Xn = vars if vars else select_next_variables(
            from_txt)
    # Calcula Xn + 1 a partir de las variables y Xn
    Xn1 = cal_xn1(rand_mix.a, rand_mix.c, rand_mix.m, rand_mix.Xn)
    # Almacena Xn + 1 como el nuevo Xn
    rand_mix.Xn = Xn1
    # Aumentar la cantidad de veces que se ha ejecutado rand_mix()
    rand_mix.count += 1
    # Si la cuenta es igual a m -> borra para generar nuevos números
    if rand_mix.count == rand_mix.m:
        if not vars:
            with open(from_txt + '.txt', 'r') as f:
                lines = f.readlines()
            with open(from_txt + '.txt', 'w') as f:
                f.writelines(lines[1:])
        del rand_mix.count
    # Regresa la variable dividiendo Xn + 1 entre m
    return (Xn1 / rand_mix.m) + 1e-15


def use_test(sample_size, variables, test, n=None):
    n_vars = len(variables)
    aproved_variables = []
    correct_variables = 0
    for variable in variables:
        pseudo = []
        for sample in range(sample_size):
            pseudo.append(rand_mix(vars=variable))
        rand_mix(reset_vars=True)
        test_args = (pseudo, n) if n else (pseudo, )
        if test(*test_args):
            correct_variables += 1
            aproved_variables.append(variable)
    return aproved_variables, correct_variables / n_vars, n_vars - correct_variables


def test_variables(initial_variables, sample_size):
    variables, attempts = generate_variables(initial_variables)
    print(
        f"{initial_variables} variables were generated after {attempts} attempts\n"
    )
    # Mean Test
    variables, acc, errors = use_test(sample_size, variables, check_mean_test)
    print(
        f"Mean Test Results - {initial_variables - errors} pass from {initial_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {len(variables)}\n"
    )
    # # Frequency Test
    remaining_variables = len(variables)
    variables, acc, errors = use_test(sample_size,
                                      variables,
                                      check_frequency_test,
                                      n=4)
    print(
        f"Frequency Test Results - {remaining_variables - errors} pass from {remaining_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {remaining_variables}\n"
    )
    # # Series Test
    remaining_variables = len(variables)
    variables, acc, errors = use_test(sample_size,
                                      variables,
                                      check_series_test,
                                      n=3)
    print(
        f"Frequency Test Results - {remaining_variables - errors} pass from {remaining_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {remaining_variables}\n"
    )
    # # Poker Test
    remaining_variables = len(variables)
    variables, acc, errors = use_test(sample_size, variables, check_poker_test)
    print(
        f"Frequency Test Results - {remaining_variables - errors} pass from {remaining_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {remaining_variables}\n"
    )

    for variable in variables:
        write_line_txt(*variable, 'txts/poker_variables')


if __name__ == "__main__":
    test_variables(initial_variables=500, sample_size=200)
