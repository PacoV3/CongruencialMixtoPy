from ast import literal_eval as make_tuple
from new_line_txt import write_line_txt
from var_generator import generate_values
from test import check_mean_test, check_frequency_test, check_series_test, check_poker_test
from rand_tools import uniform, pi_montecarlo


def select_next_variables(file_name):
    with open(file_name+'.txt') as f:
        line = f.readline().replace('\n', '')
    return make_tuple(line)


def cal_xn1(a, c, m, Xn):
    # Retorna el cálculo de Xn + 1 a partir de a, c, m y Xn
    return (a*Xn+c) % m


def rand_mix(reset_vars=False, from_txt='txts/variables'):
    if reset_vars:
        del rand_mix.count
        return
    # Si no existe la cuenta es igual a 0 y busca las siguientes variables y actualiza
    if not hasattr(rand_mix, 'count'):
        rand_mix.count = 0
        rand_mix.a, rand_mix.c, rand_mix.m, rand_mix.Xn = select_next_variables(
            from_txt)
    # Calcula Xn + 1 a partir de las variables y Xn
    Xn1 = cal_xn1(rand_mix.a, rand_mix.c, rand_mix.m, rand_mix.Xn)
    # Almacena Xn + 1 como el nuevo Xn
    rand_mix.Xn = Xn1
    # Aumentar la cantidad de veces que se ha ejecutado rand_mix()
    rand_mix.count += 1
    # Si la cuenta es igual a m -> borra para generar nuevos números
    if rand_mix.count == rand_mix.m:
        with open(from_txt + '.txt', 'r') as f:
            lines = f.readlines()
        with open(from_txt + '.txt', 'w') as f:
            f.writelines(lines[1:])
        del rand_mix.count
    # Regresa la variable dividiendo Xn + 1 entre m
    return Xn1 / rand_mix.m


def use_mean_test(sample_size):
    pseudo = []
    correct_variables = 0
    turn = 0
    open('txts/mean_variables.txt', 'w').close()
    while len(open('txts/variables.txt').readlines()) != 0:
        if turn % sample_size == 0 and turn != 0:
            a, c, m, seed = select_next_variables('txts/variables')
            with open('txts/variables.txt', 'r') as f:
                lines = f.readlines()
            with open('txts/variables.txt', 'w') as f:
                f.writelines(lines[1:])
            if check_mean_test(pseudo):
                correct_variables += 1
                write_line_txt(a, c, m, seed, 'txts/mean_variables')
            pseudo = []
            rand_mix(reset_vars=True)
        if len(open('txts/variables.txt').readlines()) != 0:
            pseudo.append(rand_mix())
        turn += 1
    return correct_variables / (turn // sample_size), (turn // sample_size) - correct_variables, turn // sample_size


def use_frequency_test(sample_size, n):
    pseudo = []
    correct_variables = 0
    turn = 0
    open('txts/frequency_variables.txt', 'w').close()
    while len(open('txts/mean_variables.txt').readlines()) != 0:
        if turn % sample_size == 0 and turn != 0:
            a, c, m, seed = select_next_variables('txts/mean_variables')
            with open('txts/mean_variables.txt', 'r') as f:
                lines = f.readlines()
            with open('txts/mean_variables.txt', 'w') as f:
                f.writelines(lines[1:])
            if check_frequency_test(pseudo, n):
                correct_variables += 1
                write_line_txt(a, c, m, seed, 'txts/frequency_variables')
            pseudo = []
            rand_mix(reset_vars=True, from_txt='txts/mean_variables')
        if len(open('txts/mean_variables.txt').readlines()) != 0:
            pseudo.append(rand_mix(from_txt='txts/mean_variables'))
        turn += 1
    return correct_variables / (turn // sample_size), (turn // sample_size) - correct_variables, turn // sample_size


# Just works till 3 by now
def use_series_test(sample_size, n):
    pseudo = []
    correct_variables = 0
    turn = 0
    open('txts/series_variables.txt', 'w').close()
    while len(open('txts/frequency_variables.txt').readlines()) != 0:
        if turn % sample_size == 0 and turn != 0:
            a, c, m, seed = select_next_variables('txts/frequency_variables')
            with open('txts/frequency_variables.txt', 'r') as f:
                lines = f.readlines()
            with open('txts/frequency_variables.txt', 'w') as f:
                f.writelines(lines[1:])
            if check_series_test(pseudo, n):
                correct_variables += 1
                write_line_txt(a, c, m, seed, 'txts/series_variables')
            pseudo = []
            rand_mix(reset_vars=True, from_txt='txts/frequency_variables')
        if len(open('txts/frequency_variables.txt').readlines()) != 0:
            pseudo.append(rand_mix(from_txt='txts/frequency_variables'))
        turn += 1
    return correct_variables / (turn // sample_size), (turn // sample_size) - correct_variables, turn // sample_size


def use_poker_test(sample_size):
    pseudo = []
    correct_variables = 0
    turn = 0
    while len(open('txts/series_variables.txt').readlines()) != 0:
        if turn % sample_size == 0 and turn != 0:
            a, c, m, seed = select_next_variables('txts/series_variables')
            with open('txts/series_variables.txt', 'r') as f:
                lines = f.readlines()
            with open('txts/series_variables.txt', 'w') as f:
                f.writelines(lines[1:])
            if check_poker_test(pseudo):
                correct_variables += 1
                write_line_txt(a, c, m, seed, 'txts/poker_variables')
            pseudo = []
            rand_mix(reset_vars=True, from_txt='txts/series_variables')
        if len(open('txts/series_variables.txt').readlines()) != 0:
            pseudo.append(rand_mix(from_txt='txts/series_variables'))
        turn += 1
    return correct_variables / (turn // sample_size), (turn // sample_size) - correct_variables, turn // sample_size


if __name__ == "__main__":
    # initial_variables = 500
    # generate_values(initial_variables, 'txts/variables')

    # sample_size = 200
    # # Accuracy:  0.9500, Errors: 5, Sample size: 100, Turns: 100
    # acc, errors, turns = use_mean_test(sample_size)
    # print(f"Mean Test Results - {turns - errors} pass from {initial_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {turns}\n")

    # initial_variables = turns - errors
    # n = 4
    # # Accuracy:  0.9579, Errors: 4, Sample size: 100, Turns: 95
    # acc, errors, turns = use_frequency_test(sample_size, n)
    # print(f"Frequency Test Results - {turns - errors} pass from {initial_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {turns}\n")

    # initial_variables = turns - errors
    # n = 3
    # # Accuracy:  0.9341, Errors: 6, Sample size: 100, Turns: 91
    # acc, errors, turns = use_series_test(sample_size, n)
    # print(f"Series Test Results - {turns - errors} pass from {initial_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {turns}\n")

    # initial_variables = turns - errors
    # # Accuracy:  0.9882, Errors: 1, Sample size: 100, Turns: 85
    # acc, errors, turns = use_poker_test(sample_size)
    # print(f"Poker Test Results - {turns - errors} pass from {initial_variables}\nAccuracy: {acc:6.4f}, Errors: {errors}, Sample size: {sample_size}, Turns: {turns}\n")

    r0_r1_list = []
    for times in range(100000):
        r0 = rand_mix(from_txt='txts/poker_variables')
        r1 = rand_mix(from_txt='txts/poker_variables')
        r0_r1_list.append((r0, r1))
        if times % 10000 == 0 and times != 0:
            print(pi_montecarlo(r0_r1_list), len(r0_r1_list))
