#1.los generadores genrean objetos de forma iterada según se soliciten
#uno por uno a cada vuelta de bucle

def generadorNumeros(limite):

    num = 1

    while num < limite:

        yield num*2

        num += 1

#generamos una variable para guardar el objeto iterable

sucesiones1 = generadorNumeros(6)

for i in sucesiones1:
    
    print(i)

#entrará en suspensión
sucesiones = generadorNumeros(10)

print(next(sucesiones))

print("Ahora va el siguiente valor")

print(next(sucesiones))

print("Siguiente...")

print(next(sucesiones))

print("Siguiente...")

print(next(sucesiones))


#2. (*ciudades) significa que el generador recibirá un número indeterminado de parámetros
#los objetos arrojados por yield pueden tener subelementos

def capitales(*ciudades):
    for capital in ciudades:
        for letra in capital:
            yield letra
        yield capital

capitales_devueltas = capitales("Berlín", "Hanoi", "Madrid", "Pekín")

print(next(capitales_devueltas))

print(next(capitales_devueltas))

print(next(capitales_devueltas))

print(next(capitales_devueltas))

print(next(capitales_devueltas))

print(next(capitales_devueltas))

print(next(capitales_devueltas))

print(next(capitales_devueltas))

#yield from

def capitales1(*ciudades):
    for capital in ciudades:
        yield from capital

capitales_devueltas1 = capitales1("Madrid", "Oslo", "Berlín", "Pekín")

print(next(capitales_devueltas1))

print(next(capitales_devueltas1))

print(next(capitales_devueltas1))

print(next(capitales_devueltas1))

print(next(capitales_devueltas1))

print(next(capitales_devueltas1))

print(next(capitales_devueltas1))

print(next(capitales_devueltas1))