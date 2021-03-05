def select_next_variables(n):
    prime_values = [6121, 6131, 6133, 6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211]
    c = ((2 + n % 5) * 200) + 21
    a = 10 ** (n % 2 + 2) + 1
    return {'a': a, 'c': c, 'm': prime_values[n], 'seed': n % 3}


def check_full_period(a, c, m, seed):
    list_of_Xn1 = []
    list_of_Xn1.append((a*seed+c) % m)
    for num in range(m - 1):
        Xn1 = (a*list_of_Xn1[num]+c) % m
        if Xn1 in list_of_Xn1:
            return False, num + 1
        list_of_Xn1.append(Xn1)
    return True


# for n in range(10):
#     values = select_next_variables(n)
#     print(check_full_period(values['a'],
#                             values['c'],
#                             values['m'],
#                             values['seed']),
#                             values)

print(check_full_period(5,7,8,4))
print(check_full_period(5,7,16,5))
print(check_full_period(5,7,11,5))

#                       Resultados
#      (Serie completa / valor de error) / combinación
# (False, 2039) {'a': 101, 'c': 421, 'm': 6121, 'seed': 102}
# (False, 3064) {'a': 1001, 'c': 621, 'm': 6131, 'seed': 102}
# (False, 6131) {'a': 101, 'c': 821, 'm': 6133, 'seed': 102}
# (False, 6141) {'a': 1001, 'c': 1021, 'm': 6143, 'seed': 102}
# (False, 6149) {'a': 101, 'c': 1221, 'm': 6151, 'seed': 102}
# (False, 6161) {'a': 1001, 'c': 421, 'm': 6163, 'seed': 102}
# (False, 6171) {'a': 101, 'c': 621, 'm': 6173, 'seed': 102}
# (False, 3097) {'a': 1001, 'c': 821, 'm': 6197, 'seed': 102}
# (False, 2065) {'a': 101, 'c': 1021, 'm': 6199, 'seed': 102}
# (False, 3100) {'a': 1001, 'c': 1221, 'm': 6203, 'seed': 102}
