class Vehiculo():

    def __init__(self, color, ruedas, ancho, alto):

        self.color = color
        self.ruedas = ruedas
        self.ancho = ancho
        self.alto = alto

    def arranca(self):
        return "vehículo el movimiento"
    

    def acelera(self):
        return "Aceleración 5 km/h"
    
    def freno(self):
        return "El vehículo ha frenado"
    
    def gira(self, direccion):
        if direccion == "derecha":
            return "Giro a la derecha"
        else:
            return "Giro a la izquierda"
        
    def getDatos(self):
        return "Color: "+self.color+" Ruedas: "+str(self.ruedas)+" Ancho: "+str(self.ancho)+" Alto: "+str(self.alto)
        

class Coche(Vehiculo):

    def __init__(self, color, ruedas, ancho, alto, carga, cilindraje, marchas, asientos, ac):
        super().__init__(color, ruedas, ancho, alto)
        self.carga = carga
        self.cilindraje = cilindraje
        self.marchas = marchas
        self.asientos = asientos
        self.ac = ac

    def cargo(self):
        return "El coche lleva una carga de: "+str(self.carga)
    
    def derrapa(self):
        return "El coehc ha derrapado"
    
    def atras(self):
        return "El coche va marcha atrás"
    
    def getDatos(self):
        return super().getDatos() + " Carga: "+str(self.carga)+" Cilindraje: "+str(self.cilindraje)+\
            " Marchas: "+str(self.marchas)+" Asientos: "+str(self.asientos)+" AC: "+str(self.ac)
    
    

class Furgoneta(Coche):

    def __init__(self, color, ruedas, ancho, alto, carga, cilindraje, marchas, asientos, ac):
        super().__init__(color, ruedas, ancho, alto, carga, cilindraje, marchas, asientos, ac)

    def getDatos(self):
        return super().getDatos()


class Bici(Vehiculo):

    def __init__(self, color, ruedas, ancho, alto):
        super().__init__(color, ruedas, ancho, alto)

    def salta(self):
        return "Ha saltado"
    
    def getDatos(self):
        return super().getDatos()
    
class Moto(Bici):

    def __init__(self, color, ruedas, ancho, alto, cilindraje):
        super().__init__(color, ruedas, ancho, alto)
        self.cilindraje = cilindraje

    def getDatos(self):
        return super().getDatos()+" Cilindraje: "+str(self.cilindraje)


furgo = Furgoneta("Rojo", 4, 6, 5, 900, 1650, 5, 5, True)
print(furgo.acelera())
print(furgo.cargo())
print(furgo.gira("Izquierda"))
print(furgo.getDatos())

moto = Moto("Azul", 2, 2, 3, 250)
print(moto.arranca())
print(moto.salta())
print(moto.getDatos())






        