import mysql.connector

conexion = mysql.connector.connect(host="localhost", database="empresa", user="root", password="")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM EMPLOYEES")

list_employees = cursor.fetchall()


for i in list_employees:
    print(f"""
ID: {i[0]}
Name: {i[1]}
Last Name: {i[2]}
Identification: {i[3]}
Department: {i[4]}
Position: {i[5]}
City: {i[6]}
Phone: {i[7]}
------------------------
""")
conexion.commit()

cursor.close()

conexion.close()