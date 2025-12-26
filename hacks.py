import operator

#1. En Python, isinstance(obj, tipo) es una función que sirve para comprobar
# si un objeto (obj) es de un tipo/clase en particular.

#isinstance(objeto, Clase_o_Tipo)
isinstance(str, int)
#Devuelve True si el objeto es una instancia del tipo o clase especificada, o
# de una subclase de esa clase.

print(isinstance(5, int))        # True  (5 es un entero)
print(isinstance(3.14, float))   # True  (3.14 es float)
print(isinstance("hola", str))   # True  (es string)
print(isinstance([1,2,3], list)) # True  (es lista)
print(isinstance(5, float))      # False (5 no es float)
print(isinstance(5, (int, float))) # True (5 es int o float)

#Usando varios tipos Puedes pasar una tupla de tipos y Python revisa si el
# objeto coincide con alguno:

print(isinstance(5, (int, float)))   # True (porque 5 es int)
print(isinstance(3.14, (int, float)))# True (porque 3.14 es float)
print(isinstance("hola", (int, float))) # False (no es ni int ni float)
print(isinstance([1,2,3], (list, dict))) # True (porque es lista)
print(isinstance({"a":1}, (list, dict))) # True (porque es diccionario)
print(isinstance((1,2), (list, dict)))   # False (no es ni lista ni diccionario)

#resultado.is_integer() → comprueba si ese decimal tiene parte decimal 0 (ej: 5.0).
def mostrar_resultado(resultado):
    # Si el número es un float como 5.0 → lo convertimos a int
    #resultado.is_integer() → comprueba si ese decimal tiene parte decimal 0 (ej: 5.0).
    if isinstance(resultado, float) and resultado.is_integer():
        return str(int(resultado))
    else:
        return str(resultado)
    

#2. eval
resultado = eval("10/21")   # Ejemplo
print(mostrar_resultado(resultado))  # Muestra "5" en lugar de "5.0"
resultado = eval("10/2")  # → 5.0
pantalla = mostrar_resultado(resultado)
print(eval("50"+"/"+"2"))
print("5x2")


#3. isinstance() y type() parecen similares, pero no hacen lo mismo.
# type() devuelve el tipo exacto del objeto, mientras que isinstance() verifica
# si el objeto es una instancia de una clase o de una subclase.

x = 5
print(type(x))         # <class 'int'>
print(type(x) == int)  # True
print(isinstance(x, int)) # True

#Pero type() no considera herencia. Si un objeto es de una clase hija, no se 
# considera del tipo de la clase padre.

class Animal: pass
class Perro(Animal): pass

mi_perro = Perro()

print(type(mi_perro) == Animal)  # False ❌
print(type(mi_perro) == Perro)   # True ✅
print(isinstance(mi_perro, Animal)) # True ✅
print(isinstance(mi_perro, Perro))  # True ✅

#isinstance entiende la herencia, mientras que type() no.
#Por eso, para comprobar tipos y herencias, es mejor usar isinstance().
#4. isinstance() también puede verificar múltiples tipos a la vez pasando
# una tupla de tipos.

print(isinstance(mi_perro, Perro))   # True ✅
print(isinstance(mi_perro, Animal)) # True ✅ (porque Perro hereda de Animal)
print(isinstance(mi_perro, (Perro, Animal))) # True ✅
print(isinstance(mi_perro, (str, list)))   # False ❌

#Return 
#el return sirve para terminar la ejecución de la función que contiene ese código
# inmediatamente, sin ejecutar nada más que esté después.
print("return al final de la función")
def coma():
    texto = "hola, Diana"
    for i in texto:
            if i == ",":
                return
            
    print("No hay coma en el texto")
            
#ops
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "=": operator.eq}

a = 5
b = 2
c = ops["+"](a, b)  # Suma 5 + 2
d = ops["-"](a, b)  # Resta 5 - 2
e = ops["*"](a, b)  # Multiplica 5 * 2
f = ops["/"](a, b)  # Divide 5 / 2

#operador Walrus :=
#El operador Walrus (:=) permite asignar valores a variables como parte de una expresión

x = "Python"
print(x)
print(type(x))

# Salida:
# Python
# <class 'str'>

#En sólo dos líneas. Como podemos ver, el uso de := asigna y devuelve el contenido de la variable.

print(x := "Python")
print(type(x))
# Python
# <class 'str'>

lista = []
entrada = input("Escribe algo: ")
while entrada != "terminar":
    lista.append(entrada)
    entrada = input("Escribe algo: ")
    
print(lista)

#con walrus
lista = []
while (entrada := input("Escribe algo: ")) != "terminar":
    lista.append(entrada)

print(lista)

#Uso de *args
#El principal uso de *args y **kwargs es en la definición de funciones.
# Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir
# una función cuyo número de parámetros de entrada puede ser variable, considera el uso
# de *args o **kwargs como una opción

def test_var_args(f_arg, *argv):
    print("primer argumento normal:", f_arg)
    for arg in argv:
        print("argumentos de *argv:", arg)

test_var_args('python', 'foo', 'bar')

#Salida
# primer argumento normal: python   
# argumentos de *argv: foo
# argumentos de *argv: bar



def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#Salida
# Hello 
# Welcome
# to
# GeeksforGeeks



#Uso de **kwargs
#**kwargs permite pasar argumentos de longitud variable asociados con un nombre o key a
# una función. Deberías usar **kwargs si quieres manejar argumentos con nombre como entrada
# a una función.

def test_var_kwargs(f_arg, **kwargs):
    print("primer argumento normal:", f_arg)
    for key, value in kwargs.items():
        print("argumentos de **kwargs: %s: %s" % (key, value))
test_var_kwargs('python', first='foo', second='bar', third='baz')
#Salida
# primer argumento normal: python
# argumentos de **kwargs: first: foo
# argumentos de **kwargs: second: bar
# argumentos de **kwargs: third: baz


def saludame(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

saludame(nombre="Covadonga")
#nombre = Covadonga


def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

print(introduce(Name="Alice", Age=25, City="New York"))


def student_info(*args, **kwargs):
    print("Subjects:", args)        # Positional arguments
    print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")
print("-----")
print(student_info("Math", "Science", Name="Bob", Age=22))

#*args hace que la función acepte cualquier número de argumentos posicionales,
# y **kwargs hace que acepte cualquier número de argumentos con nombre (keyword arguments).
#uso de unicode
#Unicode es un estándar de codificación de caracteres que permite representar texto
# de múltiples idiomas y símbolos especiales en sistemas informáticos.
# En Python, las cadenas de texto (strings) son Unicode por defecto en Python 3.x.
# Esto significa que puedes usar caracteres de diferentes idiomas y símbolos sin preocuparte
# por problemas de codificación.
#Por ejemplo:
texto = "Hola, ¿cómo estás? 😊"
print(texto)
#Salida: Hola, ¿cómo estás? 😊

print(u"\u00A9 2024")  # Símbolo de copyright
#Salida: © 2024
