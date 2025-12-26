#1.

texto = "Hola, Python"

for i in range(len(texto)):
	print(texto[i])
	

#2.*****************************************************************************************************

inputDato = input("Ingresa un dato a buscar: ")

lista = ["Ana", 5, 68, "25641", "John", "House", "Stronger"]
contador = 0

for i in lista:
	if i == inputDato:
		print("El dato ", inputDato, " existe en la lista")
		break
	else:
		contador += 1

if contador == len(lista):
	print("El dato ", inputDato, " no está en la lista")
	


#3.****************************************************************************************************

for i in range(0,3):
	print(i)




#4.Comprobar si una lista es idéntica a otra***********************************************************

def listas(lista1, lista2):
	if len(lista1) != len(lista2):
		return print("Las listas son diferentes")
	else:
		for i in range(len(lista1)):
			if lista1[i] != lista2[i]:
				return print("Las listas son diferentes")			
	return print("Las listas son iguales")
	

				
	
lista = ["Ana", 55, "Juan", "John", "Manuel", 874]
lista1 = ["Ana", 55, "Juan", "John", "Manuel", "Miguel"]
lista2 = [22, 55, "Alba"]
lista3 = ["Ana", 55, "Juan", "John", "Manuel", 874]

listas(lista, lista1)


#5.ejercicio números primos******************************************************************************

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
			
#opción 2

def listaPrimos2(a, b):
	order = range(a, b)
	if a > b:
		order = range(b, a)
	
	for i in order:
		if i == 1 or i == 2:
			print(i)
		for j in range(2,i):
			if i%j == 0:
				break
			elif j == i-1:
				print(i)
		


listaPrimos2(20,10)