import math

#1.

def divide():

    try:
        a = float(input("Introduce un número a: "))
        b = float(input("Introduce un número b: "))
        print("RESULTADO: " + str(a/b))
    except ZeroDivisionError:
        print("No existe la división entre cero")
    except ValueError:
        print("El valor introducido no es correcto")
    except:
        print("El valor introducido no es correcto")


divide()

#2. Para excepciones generales
def divide1():

    try:
        a = float(input("Introduce un número a: "))
        b = float(input("Introduce un número b: "))
        print("RESULTADO: " + str(a/b))
    except:
        print("El valor introducido no es correcto")

divide1()

#3.finally funciona como el java, que sí o sí se ejecuta
def divide2():

    try:
        a = float(input("Introduce un número a: "))
        b = float(input("Introduce un número b: "))
        print("RESULTADO: " + str(a/b))
    except:
        print("El valor introducido no es correcto")
    finally:
        print("se ha ejecutado el programa")

divide2()



#4.Puede ir sólo el finally
def divide3():

    try:
        a = float(input("Introduce un número a: "))
        b = float(input("Introduce un número b: "))
        print("RESULTADO: " + str(a/b))
    finally:
        print("se ha ejecutado el programa")

divide3()


#5. Lanzamiento de excepciones con raise forzosamente. El error que genera me oblica a poner
#el print(raiz(numeroUser)) dentro de un try catch
#el raise obliga a crear una llamada al try, un control de errores

def raiz(numero):

    if numero <0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(numero)
    
numeroUser = int(input("Introduce un número"))

try:
    print(raiz(numeroUser))
except ValueError:
    print("Error número negativo")