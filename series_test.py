def check_series_test(mean_rand_list, n):
    chi_vals = [3.84, 5.99, 7.81, 9.49, 11.07,
                12.59, 14.07, 15.51, 19.92, 18.31]
    N = len(mean_rand_list)
    val = 1 / n
    FE = (N - 1) / n ** 2
    fo = [0] * n ** 2
    X = mean_rand_list[0:-1]
    y = mean_rand_list[1:]

    for num in range(len(X)):
        for row in range(n):
            for col in range(n):
                if (val * col <= X[num] < val * (col + 1)) and (val * row <= y[num] < val * (row + 1)):
                    fo[row * n + col] += 1
                    break

    squares = [(num - FE) ** 2 for num in fo]
    chi_0 = n ** 2 / (N - 1) * sum(squares)
    chi_alpha_lib = chi_vals[n ** 2 - 2]
    return chi_0 < chi_alpha_lib
