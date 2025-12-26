import random

#El usuario intenta adivinar el número 
numeroAleatorio = random.randint(1, 100)
numeroUsuario = int(input("Introduce un número entre 1 y 100 "))


while numeroUsuario != numeroAleatorio:
    if numeroAleatorio < numeroUsuario:
        print("El número es menor a "+str(numeroUsuario))
        numeroUsuario = int(input("Introduce un número entre 1 y 100 "))
    elif numeroAleatorio > numeroUsuario:
        print("El número es mayor a "+str(numeroUsuario))
        numeroUsuario = int(input("Introduce un número entre 1 y 100 "))

print("¡Has adivinado!, el número es ---> "+str(numeroAleatorio))