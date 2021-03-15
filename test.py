from math import sqrt


# list_pseudo = [0.1344,0.124145,0.31455335,...]
def check_mean_test(list_pseudo):
    EXPECTED_MEAN = 0.5
    Z_VALUE = 1.96
    # Promedio
    observed_mean = sum(list_pseudo) / len(list_pseudo)
    # Cálculo de Z0
    z0 = (observed_mean - EXPECTED_MEAN) * sqrt(len(list_pseudo)) / sqrt(1/12)
    # Comparación
    return abs(z0) < Z_VALUE


def check_frequency_test(mean_rand_list, n):
    chi_vals = [3.84, 5.99, 7.81, 9.49, 11.07,
                12.59, 14.07, 15.51, 19.92, 18.31]
    N = len(mean_rand_list)
    val = 1 / n
    FE = N / n
    fo = [0] * n
    for rand_num in mean_rand_list:
        for i in range(n):
            if val * i <= rand_num < val * (i + 1):
                fo[i] += 1
                break
    squares = [(num - FE) ** 2 for num in fo]
    chi2_0 = sum(squares) / FE
    chi2_alpha_lib = chi_vals[n - 2]
    return chi2_0 < chi2_alpha_lib


def check_series_test(freq_rand_list, n):
    chi_vals = [3.84, 5.99, 7.81, 9.49, 11.07,
                12.59, 14.07, 15.51, 19.92, 18.31]
    N = len(freq_rand_list)
    val = 1 / n
    FE = (N - 1) / n ** 2
    fo = [0] * n ** 2
    X = freq_rand_list[:-1]
    y = freq_rand_list[1:]
    for num in range(len(X)):
        for row in range(n):
            for col in range(n):
                if (val * col <= X[num] < val * (col + 1)) and (val * row <= y[num] < val * (row + 1)):
                    fo[row * n + col] += 1
                    break
    squares = [(num - FE) ** 2 for num in fo]
    chi2_0 = n ** 2 / (N - 1) * sum(squares)
    chi2_alpha_lib = chi_vals[n ** 2 - 2]
    return chi2_0 < chi2_alpha_lib


def check_poker_test(series_rand_list):
    chi_vals = [3.84, 5.99, 7.81, 9.49, 11.07,
                12.59, 14.07, 15.51, 19.92, 18.31]
    N = len(series_rand_list)
    probabilities = [0.0001, 0.0045, 0.009, 0.072, 0.108, 0.504, 0.3024]
    fe = [N * p for p in probabilities]
    breakdown = [str(rand_num)[2:7] for rand_num in series_rand_list]
    # Add missing zeroes
    for index in range(len(breakdown)):
        while len(breakdown[index]) < 5:
            breakdown[index] += '0'
    # Fill counting
    counting = []
    for num5 in breakdown:
        temp_row = [0] * 10
        for str_num_val in num5:
            temp_row[int(str_num_val)] += 1
        counting.append(temp_row)
    # Fill FO
    fo = [0] * 7
    for row in counting:
        if 5 in row:
            fo[0] += 1
        elif 4 in row:
            fo[1] += 1
        elif 3 in row and 2 in row:
            fo[2] += 1
        elif 3 in row:
            fo[3] += 1
        elif row.count(2) == 2: 
            fo[4] += 1
        elif 2 in row:
            fo[5] += 1
        else:
            fo[6] += 1
    # Pendiente de explicar
    temp_fe = 0
    temp_fo = 0
    acc_fe = 0
    acc_fo = 0
    count = 0
    while acc_fe < 5:
        temp_fe = fe[count]
        temp_fo = fo[count]
        acc_fe += temp_fe
        acc_fo += temp_fo
        count += 1
    acc_fe -= temp_fe
    acc_fo -= temp_fo
    cat_list = [(fe[index] - fo[index]) ** 2 / fe[index] for index in range(count - 1,7)]
    chi2_0 = sum(cat_list) + ((acc_fe - acc_fo) ** 2 / acc_fe)
    chi2_alpha_lib = chi_vals[7 - count]
    return chi2_0 < chi2_alpha_lib
    
# check_poker_test([0.1937657961, 0.7118786858, 0.3588879528, 0.09856781803, 0.6368997473, 0.4945240101, 0.5947767481, 0.2224094356, 0.1769165965, 0.2030328559, 0.3917438922, 0.6908171862, 0.7228306655, 0.8896377422, 0.1272114575, 0.101937658, 0.3386689132, 0.8879528222, 0.2763268745, 0.4052232519])

# print(check_poker_test([0.70895, 0.02788, 0.90145, 0.35098, 0.01812, 0.49806, 0.94682, 0.34578, 0.27099, 0.94851, 0.34969, 0.40363, 0.91791, 0.26742, 0.15339, 0.86480, 0.89192, 0.74030, 0.19527, 0.63048]))

#print(check_poker_test([0.11111, 0.01111, 0.00111, 0.00012, 0.21120, 0.21320, 0.12345]))
