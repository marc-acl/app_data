from operator import sub
from functools import reduce
#1.
def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args, **kwargs):
        print("Ejecutamos la función interna")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado la ejecución de la función interna")
    return funcion_interna

@funcion_decoradora
def suma(*nums):
    print("La suma es: {}".format(sum(nums)))

@funcion_decoradora
def res(*nums):
    print("La resta es: {}".format(reduce(sub, nums)))

@funcion_decoradora
def divide(a, b):
    print("La división es: {}".format(a / b))

suma(5, 14, 2, 81, 4)
res(5, 6, 22, -2)
divide(10, 2)

#si ponemos **kwargs en la función decoradora, podemos pasar argumentos con clave valor
#si no se pasan no pasa nada

@funcion_decoradora
def capitales(**kwargs):
    for pais, capital in kwargs.items():
        print("La capital de {} es {}".format(pais, capital))


capitales(España="Madrid", Francia="París", Italia="Roma", Alemania="Berlín")