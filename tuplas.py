#Las tuplas permiten almacenar datos de diferentes tipos
#Son inmutables, no se pueden cambiar sus valores
trabajadores = (1, "Ana", 5000, True)
propiedades = (2, "Juan", 7000, False)
misPropiedades = list(propiedades) #Convertir una tupla en lista
print(trabajadores)
print(type(trabajadores))
print(type(misPropiedades))
print(misPropiedades)

#Operaciones con tuplas
#convertimos una lista en tupla
valores = [1, 2, 3, 4, 5]
misTrabajadores = tuple(valores)
print(misTrabajadores)

#x in s -- True if an item of s is equal to x, else False
print(2 in misTrabajadores)

#s.count(x) -- número total de ocurrencias de x en s
print(trabajadores.count("Ana"))


##len(s) -- length of s (Tamaño lista)
print(len(trabajadores))

#Desempaquetado de tuplas, asignar cada valor a una variable
#El número de variables debe coincidir con el número de elementos en la tupla
num, nombre, salario, activo = trabajadores
print(nombre)

#Los métodos de tipos mutables no funcionan en tuplas
#trabajadores.append(5)  -- ERROR
#sum
print("Sum, min, max, sorted, reversed, enumerate")
print(sum(misTrabajadores))


#min
print("min")
print(min(misTrabajadores))


#max
print("max")
print(max(misTrabajadores))


#sorted
print("sorted")
print(sorted(misTrabajadores))


#reversed
print("reversed")
print(list(reversed(misTrabajadores)))


#enumerate
print("enumerate")
for index, value in enumerate(misTrabajadores):
    print(index, value)


