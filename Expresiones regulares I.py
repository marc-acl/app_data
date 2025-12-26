#Expresiones regulares
import re

#Buscar un patron en una cadena de texto
texto = "Mi número de teléfono es 123-456-7890"
patron = r"\d{3}-\d{3}-\d{4}" # Patrón para un número de teléfono en formato XXX-XXX-XXXX
print("Patrón:", patron)
resultado = re.search(patron, texto)
if resultado:
    print("Número de teléfono encontrado:", resultado.group())
else:
    print("No se encontró ningún número de teléfono.")
#Salida: Número de teléfono encontrado: 123-456-7890
#Buscar todas las ocurrencias de un patron en una cadena de texto


#2
print("2 ********************************************************")
cadena = "El gato está en el tejado. Otro gato está en el jardín."
print(re.search("gato", cadena)) # Salida: <re.Match object; span=(3, 7), match='gato'>
print(re.findall("gato", cadena)) # Salida: ['gato', 'gato']
print(re.sub("gato", "perro", cadena)) # Salida: El perro está en el tejado. Otro perro está en el jardín.
#sub sirve para reemplazar
print(re.split(" ", cadena)) # Salida: ['El', 'gato', 'está', 'en', 'el', 'tejado.', 'Otro', 'gato', 'está', 'en', 'el', 'jardín.']
#split sirve para dividir una cadena en una lista


#start
#match sirve para buscar al inicio de la cadena de texto 
print(re.match("El", cadena)) # Salida: <re.Match object; span=(0, 2), match='El'>
print(re.match("gato", cadena)) # Salida: None
print(re.match("perro", cadena)) # Salida: None
print(re.match("en", cadena)) # Salida: <re.Match object; span=(0, 7), match='El gato'>
#search sirve para buscar en toda la cadena de texto
#match sirve para buscar al inicio de la cadena
texto_encontrado = re.search("gato", cadena)
print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())


#3
print("3 ********************************************************")
#Buscar un patron en una cadena de texto
#^ sirve para indicar que el patron debe estar al inicio de la cadena
#Ejemplo: buscar nombres que comienzan con la letra 'J'
lista_nombres = ["Ana", "Juan", "Pedro", "María", "José"]
patron = "^J" # Patrón para nombres que comienzan con la letra 'J'

nombres_con_j = [nombre for nombre in lista_nombres if re.match(patron, nombre)]
print("Nombres que comienzan con 'J':", nombres_con_j)
#Salida: Nombres que comienzan con 'J': ['Juan', 'José']
#nombre for nombre significa que por cada nombre en la lista de nombres, si cumple con la
# condicion de re.match(patron, nombre) se agrega a la nueva lista nombres_con_j
#re.match(patron, nombre) devuelve un objeto match si el nombre cumple con el patron
# o None si no lo cumple

#otra forma de hacerlo es con filter
nombres_con_j = list(filter(lambda nombre: re.match(patron, nombre), lista_nombres))
print("Nombres que comienzan con 'J' (usando filter):", nombres_con_j)
#Salida: Nombres que comienzan con 'J' (usando filter): ['Juan', 'José']
#filter aplica la función lambda a cada elemento de la lista y devuelve
# una lista con los elementos que cumplen la condición

#otra forma es con un ciclo for
nombres_con_j = []
for nombre in lista_nombres:
    if re.match(patron, nombre):
        nombres_con_j.append(nombre)
print("Nombres que comienzan con 'J' (usando ciclo for):", nombres_con_j)
#Salida: Nombres que comienzan con 'J' (usando ciclo for): ['Juan', 'José']

#otro bucle for
print("usando otro for")
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Ana María"]

for nombre in nombres:
    if re.findall("^Ana", nombre):
        print(f"El nombre {nombre} comienza con 'Ana'")
#Salida: El nombre Ana comienza con 'Ana'
#Salida: El nombre Ana María comienza con 'Ana'

#otro ejemplo con filter
print("usando filter")
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Ana María"]
nombres_con_ana = list(filter(lambda nombre: re.findall("^Ana", nombre), nombres))
print(nombres_con_ana)
#Salida: ['Ana', 'Ana María']


#usando el $ para buscar al final de la cadena
print("usando $")
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Ana María"]
for nombre in nombres:
    if re.findall("María$", nombre):
        print(f"El nombre {nombre} termina con 'María'")
#Salida: El nombre Ana María termina con 'María'


#usando corchetes para buscar un conjunto de caracteres
print("usando corchetes")
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Ana María", "juan", "javier", "camión", "jamón", "camion"]
for nombre in nombres:
    if re.findall("[Jj]uan", nombre):
        print(f"El nombre {nombre} contiene 'Juan' o 'juan'")
        #f sirve para formatear la cadena e insertar variables
#Salida: El nombre Juan contiene 'Juan' o 'juan'

for nombre in nombres:
    if re.findall("cami[oó]n", nombre):
        print(nombre)

print("usando $ con acento")

for nombre in nombres:
    if re.findall("[oó]n$", nombre):
        print(nombre)
#Salida: camión
#Salida: jamón
#Salida: camion

#uso de rangos
print("uso de rangos")
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Ana María", "juan", "javier", "camión", "jamón", "camion", "zuw"]
for nombre in nombres:
    if re.findall("[A-Ja-j]", nombre):
        print(nombre)
#Salida: El nombre Ana contiene letras entre A-M o a-m
#Salida: El nombre Juan contiene letras entre A-M o a-m
#Salida: El nombre María contiene letras entre A-M o a-m
#Salida: El nombre Ana María contiene letras entre A-M o a-m
#Salida: El nombre camión contiene letras entre A-M o a-m
#Salida: El nombre camion contiene letras entre A-M o a-m  
# 
# 
#más uso de rangos
print("más uso de rangos") 
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Ana María", "juan", "javier", "camión", "jamón", "camion", "zuw", "123", "456", "789", "abc", "def", "ghi"]
for nombre in nombres:
    if re.findall("[t-z]", nombre):
        print(nombre)

#más uso de rangos
print("más uso de rangos") 
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Felipe"]
for nombre in nombres:
    if re.findall("^[A-Fa-f]", nombre):
        print(nombre)
#Salida: Ana
#Salida: Juan


#uso de ignorecase
print("uso de ignorecase") 
nombres = ["Ana", "Juan", "Pedro", "María", "José", "Felipe", "ana", "juaN"]
for nombre in nombres:  
    if re.findall("[J-P]$", nombre, re.IGNORECASE):
        print(nombre)
#Salida: Ana
#Salida: Juan

#más uso de rangos
print("más uso de rangos")
nombres = ["Mad1", "Mad2", "Mad3", "Mad4", "Mad5", "Mad6"]
for nombre in nombres:
    if re.findall("mad[3-5]", nombre, re.IGNORECASE):
        print(nombre)

#Uso de rangos con negación
print("Uso de rangos con negación")
nombres = ["Mad1", "Mad2", "Mad3", "Mad4", "Mad5", "Mad6",]
for nombre in nombres:
    if re.findall("mad[^3-5]", nombre, re.IGNORECASE):
        print(nombre)

#rangos con valores numéricos y letras  
print("rangos con valores numéricos y letras")
nombres = ["Mad1", "Mad2", "Mad3", "Mad4", "Mad5", "Mad6", "madA", "madB", "madc"]
for nombre in nombres:
    if re.findall("mad[1-3A-C]", nombre, re.IGNORECASE):
        print(nombre)



#Busqueda de caracteres especiales
print("Busqueda de caracteres especiales")  
nombres = ["Ana!", "Juan?", "Pedro.", "María,", "José;", "Felipe:"]
for nombre in nombres:
    if re.findall("[!?.;,]", nombre):
        print(nombre)


#Match hace la busqueda al comenzar el texto y search en cualquier parte del texto
print("Match hace la busqueda al comenzar el texto y search en cualquier parte del texto")
texto = "Hola, mi nombre es Juan. Encantado de conocerte, Juan."
texto2 = "Mi nombre es Juan. Encantado de conocerte, Juan. Hola"
print(re.search("hola", texto, re.IGNORECASE))  # <re.Match object; span=(0,4), match='Hola'>
print(re.search("hola", texto))  # <re.Match object; span=(0,4), match='Hola'>
print(re.search("Hola", texto2))  # <re.Match object; span=(36
print(re.match("Hola", texto))  # Match object
print(re.match("Hola", texto2))  # None
print(re.findall("Juan", texto))  # ['Juan', 'Juan']
print(re.findall("Juan", texto2))  # ['Juan', 'Juan']


#uso de comodines
print("uso de comodines")
nombres = ["Ana!", "Juan?", "Pedro.", "María,", "José;", "Felipe:", "Ana María", "Ana-María", "Ana_María"]
for nombre in nombres:
    if re.findall("Ana.", nombre):
        print(nombre)
        #salida: Ana!
        #salida: Ana María
        #salida: Ana-María
        #salida: Ana_María



#uso de comodines al empezar
print("uso de comodines al empezar")
nombres = ["Ruana", "!Ana", "?Juan", ".Pedro", ",María", ";José", ":Felipe", "Ana María", "Ana-María", "Ana_María"]
for nombre in nombres:
    if re.search(".na", nombre):
        print(nombre)
        #salida: !Ana
        #salida: Ruana
        #salida: Ana María
        #salida: Ana-María

#uso de comodines con match
print("uso de comodines con match")
nombres = ["Ruana","Pedro Alana", "!Ana", "?Juan", ".Pedro", ",María", ";José", ":Felipe", "Ana María", "Ana-María", "María Ana"]
for nombre in nombres:
    #Match parece tener en cuenta sólo un caracter al inicio, a diferencia de search
    #que no importa cuantos caracteres haya antes del patrón

    if re.match(".na", nombre):
        print(nombre)
        #salida: !Ana
        #salida: Ana María
        #salida: Ana-María
        #salida: María Ana
#match solo busca al inicio de la cadena



#uso de comodines con match y search
print("uso de comodines con match y search")
code_one = "ksadhfoadsjkfn5987ajskldfnas"
code_two = "1234ksadhfoadsjkfn5987ajskldfnas"
code_three = "ksadhfoadsjkfn5987ajskldfnas5987e"
if re.search("5987", code_one):
    print("code_one: Encontrado")
else:
    print("code_one: No encontrado")


#ver página pythex.org para probar expresiones regulares