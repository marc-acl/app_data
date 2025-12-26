#1.
capitales = {"China":"Pekín", "Colombia":"Bogotá", "Argentina":"Buenos Aires", "Japón":"Tokio"}

for i in capitales:
    print(i+" : "+capitales[i])

for i, j in capitales.items():
    print(i+" : "+j)

#imprimir todos los items
print("***************************")

print(capitales.items())

#Ejercicio diccionarios y bucles

pais = input("Ingresa un país: ")
ciudad = input("Ingresa una capital: ")
paisCiudad = {pais:[ciudad]}

while pais != "salir" or ciudad != "salir":
    
    pais = input("Ingresa un país: ")

    if pais == "salir":
        break

    ciudad = input("Ingresa una ciudad: ")

    if ciudad == "salir":
        break

    elif pais in paisCiudad:
        paisCiudad[pais].append(ciudad)
        

    else:
        paisCiudad[pais] = [ciudad]

print(paisCiudad)


#opción 2

paisCiudad2 = {}

pais2 = input("Ingresa un país: ")

while pais2 != "salir":

    ciudad2 = input("Ingresa una ciudad: ")

    if pais2 in paisCiudad2:
        paisCiudad2[pais2].append(ciudad2)
    else:
         paisCiudad2[pais2] = [ciudad2]
    
    pais2 = input("Ingresa un país: ")

print(paisCiudad2)



