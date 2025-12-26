import sqlite3

conexion = sqlite3.connect('practica_bbdd/mi_bbdd.db')

cursor = conexion.cursor()

cursor.execute("DELETE FROM PRODUCTOS WHERE ID = 8")

conexion.commit()

cursor.close()

conexion.close()