import sqlite3

#Leeremos los datos de la base de datos creada en work_bbdd.py
#y mostraremos los datos por pantalla
#Establecer la conexión a la base de datos SQLite (se crea si no existe)
conexion = sqlite3.connect('practica_bbdd/mi_bbdd.db')

#Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

#Ejecutamos la instrucción sqlite de leer datos
#Con las columnas y el tipo de dato que va en ellas CTD_ARTICULO, PRECIO, SECCION
cursor.execute("SELECT * FROM PRODUCTOS")
#fetchall lee todos los registros y los devuelve en una lista de tuplas
productos = cursor.fetchall()

print(productos)

print("***********************************************************")

cursor.execute("SELECT SECCION FROM PRODUCTOS")

seccion = cursor.fetchall()

for i in seccion:
    print("Sección: ", i[0])#si le dejo sólo el i y no le pongo [0] me pone los paréntesis y las comas



for i in productos:
    print("Producto:", i[1])


#Actualizar bbdd
cursor.execute("UPDATE PRODUCTOS SET ARTICULO = 'Brrador Milan' WHERE ID = 2")

conexion.commit()

cursor.close()

conexion.close()