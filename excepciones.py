import sys

#1. si introducimos cero para la división, se dará un tiempo de ejecución, necesitaríamos manejar
#las excepciones

def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "No se puede dividir entre cero"

#con sys.exit() terminamos un programa
intentos = 0
while True:
    try:
        a = int(input("Ingresa un número a: "))
        b = int(input("Ingresa un número b: "))
        break
    except ValueError:
        intentos += 1
        print("El número no es válido, intenta de nuevo")
        if intentos == 3:
            print("Has consumido tres intentos")
            sys.exit()



operacion = input("Ingresa una operación a realizar: ")

if operacion == "suma":
   print(suma(a, b))

elif operacion == "resta":
   print(resta(a, b))

elif operacion == "multiplicación":
   print(mult(a, b))

elif operacion == "división":
   print(div(a, b))

else:
    print("La operación no es válida")


print("Código ejecutado")
