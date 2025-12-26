import math
#while
#1.
i = 0

while i < 10:
    print("hola número " + str(i))
    i+=1

print("Programa finalizado")


#2.
inputAge = int(input("Introduce tu edad"))
intentos = 1

while inputAge < 0 or inputAge > 75:
    inputAge = int(input("Ingresa una edad válida "))
    intentos += 1

    if intentos == 3:
        break #sale del bucle


if intentos >= 3:
    print("El número no es correcto")
else:
    print("Tu edad es "+str(inputAge))


#3.
inputNumber = float((input("Ingresa un número: ")))
intento = 1
redondeo = round(inputNumber)

while inputNumber < 0 or inputNumber/redondeo != 1:
    inputNumber = float((input("Ingresa un número válido: ")))
    redondeo = round(inputNumber)
    intento += 1

    if intento == 3:
        break

if intento >= 3:
    print("No se introdujo un valor correcto")

else:
    print(math.sqrt(inputNumber))