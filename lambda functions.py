import re

#Función normal para calcular el área de un triángulo

def triangle(b, h):
    return (b*h)/2

print(triangle(5, 9))


#Función area triángulo con lambda
area_triangle = lambda b, h: (b*h)/2
print(area_triangle(5, 9))
#Función lambda para sumar dos números
sumar = lambda a, b: a + b
print(sumar(3, 7))


#1.
exp = lambda b, e: b**e
print(exp(5,4))

#2.
word_one = lambda words: "¡{}!$".format(words)#"¡"+words+"!"+"$"
print(word_one("alondra"))

#3
lista = [987452, 256, 874, 999, 0.5, 17]
lista.sort()#ordena la lista
print(lista)

lista.sort(reverse=True)#ordena lista al revés
print(lista)

#4 hacemos una lista con tuplas adentro
lista_one = [(105, 35), (50, 17), (120, 6, 39), (99, 4)]
lista_one.sort()#los ordena según el primer número de cada tupla
print(lista_one)

#vamos a jugar
print("Vamos a jugar")
def suma_tuplas(t):
        sum = 0
        for i in t:
              sum += i
        return sum

def suma_tuplas2(t):
      return sum(t)

print(suma_tuplas2((lista_one[2])))
print(suma_tuplas(lista_one[2]))

#5. ordenamos la lista según una función
print("Ordenamos la lista según la suma de los elementos de cada tupla")
lista_two = [(105, 35), (50, 17), (120, 6, 39), (99, 4)]
lista_two.sort(key=suma_tuplas2)
print(lista_two)


#6. Lo hacemos con una función lambda
print("Lo hacemos con una función lambda")
sum_tup = lambda t: sum(t)
lista_two.sort(key=lambda t: sum(t))
print(lista_two)

#7. Ordenar lista por apellidos
print("Ordenar lista por apellidos")
music_list = ["Paul McCartney", "Rio Kosta", "Madonna", "Freddie Mercury", "Kendrik Lamar", "Steeven Tyler"]

def split_list(str_split):
    try:
          return str_split.split()[1]#accede al segundo elemento
    except IndexError:
          return str_split.split()[0]#si no hay segundo elemento, accede al primero

music_list.sort(key=split_list)
print(music_list)


#8. Lo hacemos con lambda
print("Lo hacemos con lambda")  
music_list.sort(key=lambda name: name.split()[-1])#accede al último elemento
print(music_list)


#ejercicio
lista_frases = ["Los lunes son los mejores días para programar", "Python es moderno", "Veremos Inteligencia Artificial más adelante"
                "Lambda simplifica el código"]

lista_frases.sort(key=lambda fr: len(fr), reverse=True)#ordena según la longitud de la frase
print(lista_frases)