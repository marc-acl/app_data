import mysql.connector
#todo es igual con los SGBD, sólo cambia la biblioteca a improtar

conexion = mysql.connector.connect(host="localhost", database="empresa", user="root", password="")

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEES (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL,
        IDENTIFICATION TEXT NOT NULL,
        DEPARTMENT TEXT NOT NULL,
        POSITION TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PHONE TEXT NOT NULL
    )'''
)

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