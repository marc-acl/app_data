#Crea un programa que pregunte por consola la renta. En función de la renta introducida, 
# el programa devolverá el texto: “A la renta (aquí iría la renta introducida) le corresponde 
# un (aquí iría el tipo impositivo) de tipo impositivo.
#Ejemplo: En caso de introducir por consola 13500, el programa devolverá el texto:
#“A la renta 13500 le corresponde un 15% de tipo impositivo”
#El programa debe permitir la introducción de rentas decimales.

def calcular_impuesto(renta):
    if renta < 12000:
        print("A la renta " + str(renta) + " le corresponde un 7% de tipo impositivo")
    elif renta >= 12000 and renta < 18000:
        print("A la renta " + str(renta) + " le corresponde un 15% de tipo impositivo")
    elif renta >= 18000 and renta < 35000:
        print("A la renta " + str(renta) + " le corresponde un 21% de tipo impositivo")
    elif renta >= 35000 and renta < 70000:
        print("A la renta " + str(renta) + " le corresponde un 35% de tipo impositivo")
    elif renta >= 70000:
        print("A la renta " + str(renta) + " le corresponde un 45% de tipo impositivo")
    else:
        print("Renta no válida")

renta_input = float(input("Introduce tu renta anual: "))
calcular_impuesto(renta_input)