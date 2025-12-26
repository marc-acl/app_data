import modulos_funciones
import funcionesModulo.mates as m

a = modulos_funciones.sumar(1, 3)

#otra forma es omitir el import y poner from modulos_funciones import sumar
#se pueden importar varios métodos
#lo haremos con la clase bucle for
#hace todo lo que esté en la clase fuera de cualquier método
#también puedo usar from metodos import*
from metodos import listas, listaPrimos

lista1 = ["Diana", "María"]
lista2 = ["María", "Diana"]
lista3 = ["Diana", "María"]

listas(lista1, lista3)
listaPrimos(20, 30)
print("*****************************************************")
#importamos desde otro paquete
#Es necesario crear el archivo __init__.py para que el paquete funcione como módulo
#si no se pone también funciona, pero para cosas más avanzadas se necesita

#from funcionesModulo.mates import*

m.listaPrimos2(4,20)


#Integral
from funcionesModulo.calculos.funcionesCalculos import*

print(integrar(5, 4, (1/3)))

#Matrices
from funcionesModulo.otrosCalculos.otros import*

a = [1, 1, 1, 1]
b = [1, 1, 2, 3]

print(matriz(a, b))





