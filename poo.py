#1.Los métodos dentro de las clases reciben como mínimo un parámetro que se llama self
#self se refiere a objetos de tipo coche es como el this de java
#pass es para hacer cosas después sin que lo que está incompleto dé error

class Coche():
    ruedas = 4
    motor = "Mercedes"
    color = "Rojo" 
    largo_chasis = 260
    velocidad = 0
    arranque = False
    seguro = True

    def inicio(self):
        self.arranque = True
        self.velocidad = 20

    def aceleracion(self, velocidad):
        return velocidad*2
    
    def arrancado(self):
        if self.arranque == True:
            return "El coche ha arrancado"
        
        else:
            return "El coche está parado"

    
#Instanciamos un objeto de tipo coche.

bugatti = Coche()

print(bugatti.color)

print(bugatti.velocidad)

print(bugatti.arranque)

bugatti.inicio()

print(bugatti.velocidad)

print(bugatti.arranque)

print(bugatti.aceleracion(500))

