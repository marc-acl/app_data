#1. Listas

#*************************1. LISTAS
trabajadores = ["Alba", "Antonio", "Miguel", 6]
trabajadores.append("Harry")
trabajadores.append(253)
print(trabajadores)
print(trabajadores[2])


#**********************************operaciones para listas mutables o inmutables**************************
#*********************************************************************************************************

misPropiedades = [1, "Japón"]

#Puede acceder al elemento por el final, usamos números negativos. Para Miguel, sería -4
print(trabajadores[-4])

#Imprimir en un rango
print(trabajadores[0:3])

#x in s -- True if an item of s is equal to x, else False
print(2 in trabajadores)


#x not in s -- False if an item of s is equal to x, else True
print(2 not in trabajadores)


#s + t -- the concatenation of s and t
print("concatenar*****************")
print(trabajadores+misPropiedades)


#s * n or n * s -- equivalent to adding s to itself n times
print(trabajadores * 2)

lists = [[]] * 3
lists[1].append(3)
print(lists)


#s[i] -- ith item of s, origin 0
print(trabajadores[2])
print(misPropiedades[1])


#########s[i:j] -- slice of s from i to j i es índice y j es posición
print("Slice------------------")
print(trabajadores[1:4])

#s[i:j:k]  -- slice of s from i to j with step k
print(trabajadores[1:6:2])

#len(s) -- length of s (Tamaño lista)
print(len(trabajadores))

#min(s) -- smallest item of s
numeros = [1, 5, 7, 15, 2, 5, 9, 128]
print(min(numeros))

#max(s) -- largest item of s
print(max(numeros))

#s.index(x[, i[, j]]) -- index of the first occurrence of x in s (at or after index i and before index j)
s = "programacion en python"


# Buscar la primera vez que aparece "p"
print("------------------Index------------------")
print(s.index("p"))

# Buscar a partir del índice 5
print(s.index("p", 5))

# Buscar en un rango
print(s.index("n", 5, 12)) 
print(numeros.index(15, 2, 6))

#s.count(x) -- número total de ocurrencias de x en s
print(numeros.count(5))

#******************************Operations defined on mutable sequence types******************************
#*********************************************************************************************************

#APPEND  s.append(x) appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
propiedades = [[] for i in range(2)]
propiedades[0].append(1)
propiedades[1].append("Loreine")
print(propiedades)


#s[i] = x -- el elemento i de s se sustituye por x
numeros[0] = "HOLA"
print(numeros)

#del s[i] -- elimina el elemento i de s
numeros2 = ["Diana", 1, 2, "HOLA", 56]
print(numeros2)
del numeros2[3]
print(numeros2)

#s[i:j] = t -- La porción de s de i a j se reemplaza por el contenido del iterable t
numeros2[3:4] = "REEM"
print(numeros2)

#del s[i:j:k] -- elimina los elementos de s[i:j:k]la lista
c = ["Hola", 5, 269, "Diana", 14, "Marcela", "Py", "Do", 521, 1, 741, 36]
print(c)
del c[5:10:2]
print(c)

#s.clear() -- removes all items from s (same as del s[:])
c.clear()
print(c)


#s.copy() -- creates a shallow copy of s (same as s[:])
c = ["Hola", 5, 269, "Diana", 14, "Marcela", "Py", "Do", 521, 1, 741, 36]
c.copy()
print(c)

#s.extend(t) or s += t -- extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)
print('EXTENDE')
c.extend(["Nuevo", 45, "Elemento"])
c += ["Otro", 78, "Más"]
print(c)


#s *= n -- updates s with its contents repeated n times
c *= 2
#print(c)

#s.insert(i, x) -- inserts x into s at the index given by i (same as s[i:i] = [x])
c.insert(2, "INSERTADO")
print("----------->", c)

#s.pop() or s.pop(i) - retrieves the item at i and also removes it from s
elemento = c.pop(5)
print(elemento)


#s.remove(x) -- removes the first item from s where s[i] is equal to x
c.remove("Hola")
print(c)

#s.reverse() -- reverses the items of s in place
c.reverse()
print(c)

#"The sum of 1 + 2 is {0}".format(1+2)
print("La suma de 1 + 2 es {0}".format(1+2))
print("La suma de {0} + {1} es {2}".format(1, 2, 1+2))
print("La suma de {a} + {b} es {c}".format(a=1, b=2, c=1+2))

#iterar for
frutas = ["manzana", "pera", "plátano"]

for fruta in frutas:
    print(fruta)


#iterar Con enumerate() (índice + valor)Esto imprime cada elemento de la lista.
#1 manzana
#2 pera
#3 plátano

frutas = ["manzana", "pera", "plátano"]

print("Con enumerate()------------------")
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)

#Iterar por índice (range)
frutas = ["manzana", "pera", "plátano"]

for i in range(len(frutas)):
    print(i, frutas[i])


#Usar comprensión de listas
frutas = ["manzana", "pera", "plátano"]
mayus = [f.upper() for f in frutas]
print(mayus)   # ['MANZANA', 'PERA', 'PLÁTANO']


#Con un while
frutas = ["manzana", "pera", "plátano"]
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

#for con else
frutas = ["manzana", "pera", "plátano"]
for fruta in frutas:
    print(fruta)
else:
    print("No hay más frutas")

#while con else
frutas = ["manzana", "pera", "plátano"]
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1
else:
    print("No hay más frutas")


#for dentro de una lista
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
impares = [x for x in range(10) if x % 2 != 0]
print(impares)  # [1, 3, 5, 7, 9]
cuadrados = [x**2 for x in range(10)]   
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
cubos = [x**3 for x in range(10)]
print(cubos)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

#for con lambda y listas
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8, 10]
triples = list(map(lambda x: x * 3, numeros))
print(triples)  # [3, 6, 9, 12, 15]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]
cubos = list(map(lambda x: x ** 3, numeros))
print(cubos)  # [1, 8, 27, 64, 125]

#for index value con listas
print("for index value con listas")
numeros = [10, 20, 30, 40, 50]
for index, value in enumerate(numeros):
    print(f"Índice: {index}, Valor: {value}")

#sum de una lista
print("sum de una lista")   
numeros = [10, 20, 30, 40, 50]
suma = sum(numeros) 
print(f"La suma de la lista es: {suma}")
#Salida: La suma de la lista es: 150





