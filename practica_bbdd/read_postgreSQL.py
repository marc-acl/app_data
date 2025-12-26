import psycopg2

conexion = psycopg2.connect(host="localhost", database="Employees", user="postgres", password="bVVIOsf.x")

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