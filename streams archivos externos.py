import io

#1. Crear archivo externo y escribir una línea
stream_write = io.open("D:\PYTHON TUTORIZADO\eggs.txt", "w", encoding = "utf-8")

stream_write.write("Hello, eggs!")

stream_write.close()


#2. Crear archivo externo y escribir varias lineas
stream_write2 = io.open("D:\PYTHON TUTORIZADO\eggs1.txt", "w", encoding = "utf-8")

stream_write2.writelines(["Hello, eggs!\n", "Hello, spam!\n", "Hello, ham!\n"])

stream_write2.close()


#3. Leemos los archivos
#NO HACE dos lecturas seguidas porque el cursor se va moviendo y si hace una se va al final
#no hay nada después del cursor, entonces una segunda lectura no arroja nada
#para desplazar el cursor usamos seek()
print("*************************eggs***************************")
stream_read = io.open("D:\PYTHON TUTORIZADO\eggs.txt", "r", encoding = "utf-8")
print(stream_read.read())

print("**********************SEGUNDA LECTURA eggs*******************************")
stream_read.seek(0)#movemos el cursor al inicio, posición 0
print(stream_read.read())

#read(i) leera hasta el caracter i y seek(i) lee a partir del caracter i
stream_read.seek(0)
print(stream_read.read(5))#lee hasta caracter 5
stream_read.seek(8) #ubica el cursor en el caracter 8
print(stream_read.read())#lee a partir del caracter 8

#Desplaza el cursor al final de la primera linea, con readLine que lee una sola linea
stream_rd = io.open("D:\PYTHON TUTORIZADO\eggs1.txt", "r", encoding = "utf-8")
stream_rd.seek(len(stream_rd.readline()))
print(stream_rd.read())#omite la primera linea
stream_rd.close()
stream_read.close()


print("*************************eggs1 ***************************")
stream_read1 = io.open("D:\PYTHON TUTORIZADO\eggs1.txt", "r", encoding = "utf-8")
print(stream_read1.read())
stream_read1.close()
print("*************************eggs1 ***************************")


#4. Lectura linea a linea con readLine que lee la primera linea
stream_read2 = io.open("D:\PYTHON TUTORIZADO\eggs1.txt", "r", encoding = "utf-8")
print(stream_read2.readline())
stream_read2.close()
print("*************************eggs1 ***************************")


#5. Lectura de todas las lineas con readlines, lo guarda en una lista
stream_read3 = io.open("D:\PYTHON TUTORIZADO\eggs1.txt", "r", encoding = "utf-8")
print(stream_read3.readlines())
stream_read3.close()

print("**************************iteramos sobre la lista******************************")
#podemos iterar sobre la lista # .strip() quita saltos de línea al final
stream_read4 = io.open("D:\PYTHON TUTORIZADO\eggs1.txt", "r", encoding = "utf-8")

for i in stream_read4.readlines():
    print(i.strip())

stream_read4.close()

#6.Agregar líneas al fichero
print("***********************APPEND*******************************")
stream_write5 = io.open("D:\PYTHON TUTORIZADO\eggs.txt", "a", encoding = "utf-8")
stream_write5.write("\nGuardamos información")
stream_write5.close()


print("***************************REEMPLAZO TEXTO**********************************************")
#reemplazamos texto hello, spam! por SE REEMPLAZO Hello, spam! por EYYYYYYYY forma 1
stream_new = io.open("D:\PYTHON TUTORIZADO\eggs2.txt", "w", encoding = "utf-8")
stream_new.write("Hola, Diana")
stream_new.write("\nTodo estará bien")
stream_new.write("\nconfía siempre")
stream_new.close()

#reemplazo opción 1
stream_replace = io.open("D:\PYTHON TUTORIZADO\eggs2.txt", "r+", encoding = "utf-8")
contenido = stream_replace.read()
contenido = contenido.replace("Todo estará bien", "EYYYYYYYY")
stream_replace.seek(len(stream_replace.readline()))#mueve el cursor al final de la primera linea
stream_replace.write(contenido)
stream_replace.truncate()#trunca el archivo, elimina lo que queda después del cursor
stream_replace.seek(0)
print(stream_replace.read())
stream_replace.close()

#opción 2 para reemplazar
stream_new1 = io.open("D:\PYTHON TUTORIZADO\eggs3.txt", "w", encoding = "utf-8")
stream_new1.write("Hola, Diana")
stream_new1.write("\nTodo estará bien")
stream_new1.write("\nconfía siempre")
stream_new1.close()

#reemplazo opción 2
stream_new2 = io.open("D:\PYTHON TUTORIZADO\eggs3.txt", "r", encoding = "utf-8")
print(stream_new2.read())
stream_new2.close()
print("")
stream_replace1 = io.open("D:\PYTHON TUTORIZADO\eggs3.txt", "r+", encoding = "utf-8")
lista = stream_replace1.readlines()
lista[1] = "REEEMPLAZOOOOO \n"
stream_replace1.seek(0)
stream_replace1.writelines(lista)
stream_replace1.truncate()
stream_replace1.close()














