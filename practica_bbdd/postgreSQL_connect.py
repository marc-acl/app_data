import psycopg2

conexion = psycopg2.connect(host="localhost", database="Employees", user="postgres", password="bVVIOsf.x")

cursor = conexion.cursor()

cursor.execute("""
    INSERT INTO employees (
        NAME, LAST_NAME, IDENTIFICATION, DEPARTMENT, POSITION, CITY, PHONE
    ) VALUES (
        'María Isabel', 'Saavedra Morris', 'Z145455D', 'Research', 'Psychology', 'Madrid', '647892123'
    )
""")


conexion.commit()

cursor.close()

conexion.close()