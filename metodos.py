def listas(lista1, lista2):
	if len(lista1) != len(lista2):
		return print("Las listas son diferentes")
	else:
		for i in range(len(lista1)):
			if lista1[i] != lista2[i]:
				return print("Las listas son diferentes")			
	return print("Las listas son iguales")


def listaPrimos(a, b):
	
	order = range(a, b)
	if a > b:
		order = range(b, a)
	
	for i in order:
		divisibles = 0
		for j in range(1,i+1):
			if i%j == 0:
				divisibles += 1
		if divisibles == 2 or i == 1:
			print(i)
			
