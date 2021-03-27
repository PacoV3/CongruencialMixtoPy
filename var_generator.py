# http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
from timeit import timeit
from time import time
from new_line_txt import write_line_txt


# aproximadamente 350 combinaciones correctas en 1000 vueltas
def select_next_variables():
	"""
	Funcion para la seleccion de variables
	"""
	time_var = int(time() * 1000000)
	# Lista de posibles m
	prime_values = [
		11593, 11597, 11617, 11621, 11633, 11657, 11677, 11681, 11689, 11699,
		11701, 11717, 11719, 11731, 11743, 11777, 11779, 11783, 11789, 11801,
		11807, 11813, 11821, 11827, 11831, 11833, 11839, 11863, 11867, 11887,
		11897, 11903, 11909, 11923, 11927, 11933, 11939, 11941, 11953, 11959,
		11969, 11971, 11981, 11987, 12007, 12011, 12037, 12041, 12043, 12049,
		12071, 12073, 12097, 12101, 12107, 12109, 12113, 12119, 12143, 12149,
		12157, 12161, 12163, 12197, 12203, 12211, 12227, 12239, 12241, 12251,
		12253, 12263, 12269, 12277, 12281, 12289, 12301, 12323, 12329, 12343,
		12347, 12373, 12377, 12379, 12391, 12401, 12409, 12413, 12421, 12433,
		12437, 12451, 12457, 12473, 12479, 12487, 12491, 12497, 12503, 12511,
		12517, 12527, 12539, 12541, 12547, 12553, 12569, 12577, 12583, 12589,
		12601, 12611, 12613, 12619, 12637, 12641, 12647, 12653, 12659, 12671,
		12689, 12697, 12703, 12713, 12721, 12739, 12743, 12757, 12763, 12781,
		12791, 12799, 12809, 12821, 12823, 12829, 12841, 12853, 12889, 12893,
		12899, 12907, 12911, 12917, 12919, 12923, 12941, 12953, 12959, 12967,
		12973, 12979, 12983, 13001, 13003, 13007, 13009, 13033, 13037, 13043,
		13049, 13063, 13093, 13099, 13103, 13109, 13121, 13127, 13147, 13151,
		13159, 13163, 13171, 13177, 13183, 13187, 13217, 13219, 13229, 13241,
		13249, 13259, 13267, 13291, 13297, 13309, 13313, 13327, 13331, 13337,
		13339, 13367
	]
	# a y c siguen el consejo del libro
	a = 10**(time_var % 3 + 2) + 1
	c = ((time_var % 7) * 200) + 21
	# Tomar un index a partir de el tiempo actual
	index = time_var % len(prime_values)
	# Regresar los valores
	return (a, c, prime_values[index], time_var % prime_values[index])


def check_full_period(a, c, m, seed):
	"""
	Funcion para checar el periodo
	"""
	# Igualamos el primer valor de la lista por Xn
	Xn = (a * seed + c) % m
	list_of_Xn1 = {Xn}
	# Por cada numero antes de m - 2
	for _ in range(m - 2):
		# Calculamos Xn1
		Xn1 = (a * Xn + c) % m
		# Si Xn1 esta en el listado regresa False
		if Xn1 in list_of_Xn1:
			return False
		# Agrega Xn1 a la lista de Xn y actualiza el valor de Xn para la siguiente vuelta
		Xn = Xn1
		list_of_Xn1.add(Xn1)
	# Si no se encontraron repetidos regresa True
	return True


def generate_variables(n):
	"""
	Funcion para generar variables a partir de vueltas
	"""
	variables = []
	attempts = 0
	while len(variables) < n:
		attempts += 1
		a, c, m, seed = select_next_variables()
		if check_full_period(a, c, m, seed):
			variables.append((a, c, m, seed))
	return variables, attempts


if __name__ == "__main__":
	# python3 -m timeit -n 1000 -s 'from var_generator import generate_variables' 'generate_variables(1)'
	print(timeit(lambda: generate_variables(1), number=1000))
