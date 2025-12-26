#1. Variables
#2. Print
#3. Constantes
#4.Concatenación
#5. String (String largo)

#**********************************1. Variables
mensaje = "Hola mundo"
print(mensaje)
mensaje = "Hemos cambiado"
print(mensaje)
mensaje = 5
print(mensaje)

numero1 = 3
numero2 =16

#***********************************2. Print
print(numero1+numero2)
print(numero1-numero2)
print(numero1%numero2)
print(numero1/numero2)


#3. CONSTANTES
#Se declaran con mayúculas, sin embargo se deja cambiar.
#Realmente se usan en mayúsculas para que la gente sepa que no se debencambiar
#Lo que se hace es declararse en un archivo externo en donde no se puedan cambiar

NUMERO3 = 15
NUMERO3 = 2
print(NUMERO3)


#****************************4. CONCATENAR

#Sólo se permiten concatenar Strings

nombre = "Juana"
edad = 18
salario = 2050
comision = 230 
print("Mi nombre es "+nombre)

#También podemos usar comillas simples, esto por el anidamiento de comillas
print('Mi nombre es '+nombre)

#con str() convertimos a texto lo que hay dentro de los paréntesis
print("Mi nombre es "+nombre+" y tengo "+str(edad)+" años")
print("Mi nombre es "+nombre+" y tengo",edad,"años")

#Cuando se usan sólo valores numéricos, el + suma
print(salario+comision)

#***********************************5. String
#Cuando el String es muy largo, se pone entre tres comillas
texto = """What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer
took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,
into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the
release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum."""