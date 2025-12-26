import io

file = io.open(r"D:\PYTHON TUTORIZADO\11.Archivos externos\clientes\clientes.txt", "r", encoding="utf-8")
#print(file.readable())


for line in file.readlines():#lee línea a línea y las devuelve en una lista
    line = line.split(";")#split devuelve una lista
    line = "Articulo = " + line[0] + " "+ "Nombre = " + line[1] + " " + "Dirección = " + line[2] + " " + "Población = " + line[3]+\
    " " + "Teléfono = " + line[4] + " "+ "Responsable =" + line[5].strip()#strip elimina los espacios en blanco al final
    print(line)

    

file.close()