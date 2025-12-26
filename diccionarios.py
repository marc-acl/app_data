#Diferentes formas de crear diccionarios
capitales = {"España": "Madrid", "Francia": "París", "Reino Unido": "Londres"}
a = dict(one = 1, two = 2, three = 3, four = "hola")
b = dict(zip(['Hello', 'Bye', 'python'], [1, 2, 3]))
c = dict([('Hola', 1), ('Adiós', 2), ('Java', 3)])
d = dict({'Hola': 1, 'Adiós': 2, 'Java': 3})
e = dict({'Hola': 1, 'Adiós': 2, 'Java': 3}, two = 2, four = "hola")


print(capitales)
print(a)
print(b)
print(c)
print(d)
print(e)

#Agregar elementos a un diccionario
capitales["Alemania"] = "Berlín"

#Cambiar el valor de una clave
capitales["España"] = "Barcelona"

#Eliminar un elemento del diccionario
del capitales["Reino Unido"]
print(capitales)

#Podemos guardar diferentes tipos de datos en un diccionario
datos = {"Nombre": "Ana", 100 : "comisiones", True: "Activo", 3.5: "Salario", "Propiedades" : 1250.75}
print(datos)

#list(d) -- Return a list of all the keys used in the dictionary d.
print(list(datos))

#len(d) -- Return the number of items in the dictionary d.
print(len(datos))

#d[key] -- Return the item of d with key key. Raises a KeyError if key is not in the map.
print(datos["Nombre"])

#d[key] = value -- Set d[key] to value.
datos["Nombre"] = "María"
print(datos["Nombre"])

#del d[key] -- Remove d[key] from d. Raises a KeyError if key is not in the map.
del datos[3.5]
print(datos)

#key in d -- Return True if d has a key key, else False.
print(100 in datos)
print("Salario" in datos)

#key not in d -- Equivalent to not key in d.
print(3.5 not in datos)
print("María" not in datos)

#iter(d) -- Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).
for key in iter(datos):
    print(key)

#copy() -- Return a shallow copy of the dictionary.
datos2 = datos.copy()
print(datos2)

#clear() -- Remove all items from the dictionary.
datos.clear()
print(datos)


#get(key[, default]) -- Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
print(datos2.get("Nombre"))
print(datos2.get("Salario", "No existe"))


#items() -- Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
print(datos2.items())

#keys() -- Return a new view of the dictionary’s keys. See the documentation of view objects.
print(datos2.keys())

#pop(key[, default]) -- Remove specified key and return the corresponding value. If key is not found, default is returned if given, otherwise KeyError is raised.
print(datos2.pop("Nombre"))
print(datos2.pop("Nombre", "No existe"))

#popitem() -- Remove and return a (key, value) pair as a 2-tuple. Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.
print(datos2.popitem())

#reversed(d) -- Return a reverse iterator over the keys of the dictionary. This is a shortcut for reversed(d.keys()).
for key in reversed(datos2):
    print(key)
print(reversed(datos2))
#salida: <dict_reversekeyiterator object at 0x0000021C1B2D3F10>

#setdefault(key[, default]) -- If key is in the dictionary, return its value.
# If not, insert key with a value of default and return default. default defaults to None.
#modifica el diccionario 
print(datos2.setdefault("Nombre", "Sin nombre"))    
print(datos2.setdefault("Edad", 18))
print(datos2)

#update([other]) -- Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
#update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or
#other = {'Edad': 20, 'Salario': 2500} agrega un diccionario a otro
other = [('Edad', 20), ('Salario', 2500)]
datos2.update(other)
print(datos2)

#values() -- Return a new view of the dictionary’s values. See the documentation of view objects.
print(datos2.values())
print(type(datos2.values()))
print(list(datos2.values()))
print(tuple(datos2.values()))

#d ||= other -- Update d with the key/value pairs from other, overwriting existing keys. This is equivalent to d.update(other).
#This operator was added in Python 3.9. It is not supported in earlier versions. Agrega un diccionario a otro
datos2 |= {'Ciudad': 'Madrid', 'País': 'España'}
print(datos2)

#d = other -- Create a new dictionary initialized from the key/value pairs in other. This is equivalent to d = dict(other).
#This operator was added in Python 3.9. It is not supported in earlier versions
datos3 = {'A': 1, 'B': 2}
datos3 = {'C': 3, 'D': 4}
print(datos3)

#Poner claves en una lista y que todas tengan el mismo valor
claves = ["Colombia", "Perú", "Argentina"]
paises = dict.fromkeys(claves, "Latinoamérica")
print(paises)

#Poner claves en una lista con diferentes valores
valores = [1, 2, 3]
paises2 = dict(zip(claves, valores))
print(paises2)

#Poner claves en una lista con diferentes valores
valores2 = ["Bogotá", "Lima", "Buenos Aires"]
paises3 = dict(zip(claves, valores2))
print(paises3)

#Otra forma
paises4 = {claves[i]: valores2[i] for i in range(len(claves))}
print(paises4)

#Otra forma
paises5 = {claves[0]: valores2[0], claves[1]: valores2[1], claves[2]: valores2[2]}
print(paises5)

#Imprimir claves y valores por separado
for key, value in paises3.items():
    print(f"Clave: {key}, Valor: {value}")

#Otra forma de imprimir claves
print(paises3.keys())

#Diccionario Michael Jordan
michael_jordan = {23: "Chicago Bulls", "Nombre" : "Michael Jordan", "campeonatos" : 6, "MVP" : 5, "Anillos" : [1991, 1992, 1993, 1996, 1997, 1998], "Equipos" : {"Chicago Bulls" : [1984, 1993], "Washington Wizards" : [2001, 2003]}}
print(michael_jordan)
print(michael_jordan["Anillos"])
print(michael_jordan["Equipos"]["Chicago Bulls"])
print(michael_jordan["Equipos"]["Washington Wizards"][1])

#métodos
print("Hola", **{"end": "!!!\n"})
#Hola!!!

word1 = "list"
word2 = "casefull"
dicti = {word1:word2}
print(dicti[word1])
#casefull
print(word1, word2)
print(f"{word1} {word2}")

print('{0}{1}'.format(word1, word2))
print(dicti)
print(dicti.values)
print(dicti[word1])
#casefull
print(word1, word2)
#list casefull
print(f"{word1} {word2}")
#list casefull

for clave, valor in dicti.items():
    print(clave, valor)
    #list casefull

print(*dicti)
#list
print(*dicti.values())
#casefull

#print() solo acepta estos argumentos con nombre:

#sep

#end

#file

#flush



