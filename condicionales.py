# Condicionales en Python
# if, elif, else
#1.
def notas(nota):
    if nota>=5 and nota<=10:
        return "Aprobado"
    
    elif nota > 10 or nota < 0:
        return "Nota no válida"

    else:
        return "Suspenso :("

nota = input("Introduce la nota: ")
print(notas(int(nota)))


#2.
def edad(edad, tiempo, lentes):
    if edad >= 18 and edad <= 90:
        print("Eres mayor de edad")
        if edad >= 65 and lentes == 's':
            respuesta = input("¿Usas lentes hace más de 10 años? (s/n): ")

            if respuesta == 's':
                print("Debe usar lentes")
            else:
                print("Debe hacer el examen de la vista")

        elif edad >= 65 and lentes == 'n' and tiempo < 2:
            print("Es necesario que haga un examen de la vista")

        elif (edad < 65 or tiempo < 2) and lentes == 's':
            print("Debe hacer un examen de conducción antes de 1 año")

        else:
            print("Puede conducir")
        

    elif edad > 90 and tiempo > 30 and lentes == 'n':
        print("Debe realizar un examen de conducción cada año")

    elif edad > 90 and tiempo < 30 or lentes == 's':
        print("No puede conducir")

    elif edad < 18:
        print("Eres menor de edad")

    else:
        print("Datos no válidos")

age = int(input("Introduce tu edad: "))
tiempo = int(input("Hace cuánto tiempo conduces (en años): "))
lentes = input("¿Usas lentes? (s/n): ")
edad(age, tiempo, lentes)


