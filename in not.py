#in not

#1.
empleados = ["Miguel", "Ana", "Lucía", "Javier", "María"]
inputEmpleado = input("Introduce el nombre del empleado: ")
if inputEmpleado in empleados:
    print("El empleado", inputEmpleado, "sí trabaja en la empresa")

#También se puede not inputEmpleado in empleados
elif inputEmpleado not in empleados:
    print("El empleado", inputEmpleado, "no trabaja en la empresa")

#2.
texto = "Soy Norby y me gusta leer sobre ciencia ficción"
if "Norby" in texto:
    print("El texto contiene la palabra Norby")
else:
    print("El texto no contiene la palabra Norby")



#3.
texto2 = ("Ana", 2500, "45", "Python")

inputTxt = input("Ingresa un dato ")

if inputTxt in texto2:
    print("La tupla contiene el valor ", inputTxt)
else:
    print("El dato ", inputTxt, " no pertenece a la tupla")