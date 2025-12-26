#La indentación es muy importante en Python, ya que define bloques de código.

def imprimir_mensaje():
    print("Hola desde una función")

imprimir_mensaje()


def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("La suma es:", resultado)


def mensaje_personalizado(nombre, edad):
    return "Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años."


print(mensaje_personalizado("Carlos", 30))

