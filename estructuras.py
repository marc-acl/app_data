import queue

#1
solar_system = "Tierra Marte Venus Moon Sun Tierra Venus"
planets = set()

#El split hace que los elementos se reconozcan porque su división es lo que se pone en el paréntesis
#en este caso un espacio " "
#los sets no tienen orden de los elementos, los imprime en desorden
#Elimina los elementos repetidos

for i in solar_system.split(" "):

    planets.add(i)

print(planets)
print(len(planets))

#2.Si no especificamos la separación, separa cada elemento por coma
#{'S', 'i', 'u', 'e', 'r', 'V', 'T', ' ', 'n', 'o', 'a', 'M', 't', 's'}
planets2 = set(solar_system)
print(planets2)
print(len(planets2))


print("*********************FIFO************************************")
#3. Queue lo que se va sacando queda fuera de la cola, por defecto, con get() usa FIFO

mi_cola = queue.Queue()

mi_cola.put("Bogotá")
mi_cola.put("Berlín")
mi_cola.put("Madrid")
mi_cola.put("Tokio")

#imprime el primer elemento que entró por FIFO
print(mi_cola.get())

print("")
#Imprime los elementos restantes
print("Elementos restantes")

for i in mi_cola.queue:

    print(i)

print("")
print("*********************LIFO************************************")
#4. Queue LIFO

mi_cola2 = queue.LifoQueue()

mi_cola2.put("Marruecos")
mi_cola2.put("Turquía")
mi_cola2.put("China")
mi_cola2.put("Congo")

#imprime el último elemento que entró por FIFO
print(mi_cola2.get())

print("")
#Imprime los elementos restantes
print("Elementos restantes")
for i in mi_cola2.queue:

    print(i)

print("")

print("*********************PRIORITY************************************")
#5. Queue priority, la prioridad se tiene que especificar con el número que le asignemos
#Egipto tiene mayor prioridad porque es 1
mi_cola3 = queue.PriorityQueue()

mi_cola3.put((3, "Sudafrica"))
mi_cola3.put((1, "Egipto"))
mi_cola3.put((4, "China"))
mi_cola3.put((2, "Congo"))

#imprime el elemento de más prioridad
print(mi_cola3.get())

print("")
#Imprime los elementos restantes
print("Elementos restantes")
for i in mi_cola3.queue:

    print(i)

print("")

print("**************************LIMITE COLAS*****************************************")

#6. podemos definir el tamaño de las colas. Si meto un número diferente no hace nada
mi_cola4 = queue.Queue(5)

texto = "Barcelona Oslo Roma Florencia Hanoi"

while mi_cola4.empty():

    for i in texto.split(" "):

        mi_cola4.put(i)

print(mi_cola4.get())






