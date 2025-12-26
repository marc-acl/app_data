#1. Crea un programa que pida introducir por consola 10 nombres propios de personas. 
#• Los nombres se guardarán en una lista. 
#• Si introducimos un nombre repetido, el programa lanzará una excepción de tipo 
#ValueError, la excepción nos informará del error con el texto “Error. Este nombre ya se 
#ha introducido”, y no se guardará el nombre repetido en la lista.  
#• Imprimir el contenido de la lista por consola.

#el raise es la única forma de lanzar un error intencional

nombres = []

q = 0


while q < 10:

    inputUser = input("Ingresa un nombre: ")

    try:

        if inputUser in nombres:

            raise ValueError 
    
        else:
            
            nombres.append(inputUser)

            q += 1

    except ValueError:

        print("El nombre ya existe en la lista")

             

print(nombres)



