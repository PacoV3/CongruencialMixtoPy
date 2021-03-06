# http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
# def select_next_variables(n):
#     prime_values = [6133, 6143, 6151, 6163, 6173]
#     c = ((2 + n % 5) * 200) + 21
#     a = 10 ** (n % 2 + 2) + 1
#     return {'a': a, 'c': c, 'm': prime_values[n], 'seed': 1}


def select_next_variables(n):
    a = n + n % 10
    if a % 2 != 1:
        a += 1
    c = 421
    return {'a': a, 'c': c, 'm': 1039, 'seed': 0}


def check_full_period(a, c, m, seed):
    list_of_Xn = [seed]
    for num in range(m - 2):
        Xn1 = (a*list_of_Xn[num]+c) % m
        if Xn1 in list_of_Xn:
            return False, num
        list_of_Xn.append(Xn1)
    # f = open("output.txt", "a")
    # f.write(str(list_of_Xn) + '\n')
    # f.close()
    return True


for n in range(500):
    values = select_next_variables(n)
    print(check_full_period(values['a'],
                            values['c'],
                            values['m'],
                            values['seed']),
          values)

# print(check_full_period(5, 7, 8, 4))
# print(check_full_period(5, 7, 16, 5))
# print(check_full_period(5, 7, 11, 5))
