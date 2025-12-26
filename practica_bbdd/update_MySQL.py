import mysql.connector

conexion = mysql.connector.connect(host="localhost", database="empresa", user="root", password="")

cursor = conexion.cursor()

cursor.execute("UPDATE EMPLOYEES SET DEPARTMENT = 'Research Ph.D' WHERE ID = 1")

conexion.commit()

cursor.close()

conexion.close()