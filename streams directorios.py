import os
import io

directorio = os.makedirs("D:\PYTHON TUTORIZADO\directorio")
archivo = io.open("D:\PYTHON TUTORIZADO\directorio\eggs.txt", "w", encoding = "utf-8")
archivo.write("Hola, este es el primer archivo!")
archivo.close()


#getcwd() Retorna una cadena que representa el directorio de trabajo actual.

print(os.getcwd())


#os.chdir(path) Cambia el directorio de trabajo actual a path. Nos movemos entre directorios
os.chdir("D:\PYTHON TUTORIZADO\directorio")

print(os.getcwd())

#otra opción es creando el directorio, me muevo a él y creo el archivo de texto
directorio_1 = os.makedirs("D:\PYTHON TUTORIZADO\directorio_1")
os.chdir("D:\PYTHON TUTORIZADO\directorio_1")
archivo_1 = io.open("eggs_1.txt", "w", encoding = "utf-8")
archivo_1.write("Hola, este es el primer archivo eggs_1!")
archivo_1.close()

archivo_2 = io.open("eggs_2.docx", "w", encoding = "utf-8")#lo deja abrir con txt
archivo_2.write("Hola, este es el primer archivo eggs_2 de word file!")
archivo_2.close()

#listdir(path='.') Retorna una lista que contiene los nombres de las entradas en el directorio dado por path
print("*******************DIRECTORIO directorio_1**************************** ")
print(os.listdir("./"))

#renombramos un archivo
os.rename("eggs_2.docx", "archivo_rename.txt")
print("*****lista actualizada directorio_1 después de renombrar eggs_2.docx a archivo_rename txt********")
print(os.listdir("./"))

#eliminar un archivo
os.remove("eggs_1.txt")
print("*****lista actualizada directorio_1 despuès de eliminar eggs_1********")
print(os.listdir("./"))

#eliminar una carpeta con contenido en su interior.
#Primero hay que eliminar todo lo que tiene en el interior
os.chdir("D:\PYTHON TUTORIZADO\directorio")
print("**********************lista directorio***********************")
print(os.listdir("./"))
os.remove("eggs.txt")
os.chdir("../")#me muevo un nivel arriba de la raíz
os.rmdir("directorio")#borra directorio
print("******************se remueve directorio*******************")

#verificamos la existencia de un archivo y elminamos
os.chdir(r"D:\PYTHON TUTORIZADO\11.Archivos externos")
print("***********************lista en 11.Archivos externos**********************")
print(os.listdir("./"))
lista_archivos = os.listdir("./")

for file in lista_archivos:

    if file == "6":

        os.remove(file)

else:
    print("***************Únicos archivos encontrados***************************")
    print(lista_archivos)





