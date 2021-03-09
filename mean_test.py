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
