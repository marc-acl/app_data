#continue

texto = "Juan Díaz"
contador = 0
for i in texto:
    if i == "p":
        continue
    contador += 1

print(contador)


#***************************** pass ****************************************
#Se usa cuando hay algo que no queremos usar todavía. También en clases

for i in texto:
    pass

print("hola")


#****************************** else ****************************************
#Else para bucles. El flow de ejecución entra al else cuando el bucle ha terminado en su totalidad, es decir
#si se irrumpe por un break, el flujo no entra en e else

nombre = "Diana Marcela Python"

for i in nombre:
    if i == "M":
        print(True)
        break

else:
    print(False)


