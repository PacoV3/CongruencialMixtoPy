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
    chi_0 = sum(squares) / FE
    chi_alpha_lib = chi_vals[n - 2]
    return chi_0 < chi_alpha_lib
