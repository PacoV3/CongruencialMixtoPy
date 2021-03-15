# http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
from time import time
from new_line_txt import write_line_txt


# aproximadamente 350 combinaciones correctas en 1000 vueltas
def select_next_variables():
    '''
    Funcion para la seleccion de variables
    '''
    time_var = int(time() * 1000)
    # Lista de posibles m
    prime_values = [1097, 1103, 1109, 1117, 1123, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1303, 1307, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017,
                    2029, 2039, 2053, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2251, 2267, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999]
    # a y c siguen el consejo del libro
    a = 10 ** (time_var % 3 + 2) + 1
    c = ((time_var % 7) * 200) + 21
    # Tomar un index a partir de el tiempo actual
    index = time_var % len(prime_values)
    # Regresar los valores
    return (a, c, prime_values[index], time_var % prime_values[index])


def check_full_period(a, c, m, seed, file_name):
    '''
    Funcion para checar el periodo
    '''
    # Igualamos el primer valor de la lista por Xn
    Xn = (a*seed+c) % m
    list_of_Xn1 = {Xn}
    # Por cada numero antes de m - 2
    for _ in range(m - 2):
        # Calculamos Xn1
        Xn1 = (a*Xn+c) % m
        # Si Xn1 esta en el listado regresa False
        if Xn1 in list_of_Xn1:
            return False
        # Agrega Xn1 a la lista de Xn y actualiza el valor de Xn para la siguiente vuelta
        Xn = Xn1
        list_of_Xn1.add(Xn1)
    # Si no se encontraron repetidos regresa True
    return True


def generate_values(n_variables, file_name):
    '''
    Funcion para generar variables a partir de vueltas
    '''
    # Borra el contenido de variables
    open(file_name+'.txt', 'w').close()
    while len(open(file_name + '.txt').readlines()) != n_variables:
        a, c, m, seed = select_next_variables()
        if check_full_period(a, c, m, seed, file_name):
            write_line_txt(a, c, m, seed, file_name)

# generate_values(1,'variables')
