#1. Definimos el CONSTRUCTOR en python. Si el constructor no se define, python asume uno pero vacío
#se llama constructor por defecto

#ENCAPSULAR MODIFICADORES DE ACCESO
#_ Se puede usar en clases que heredan
#__ sólo se puede usar en la clase
#es obligación usar _ o __ en cualquier parte que se use la variable
#también podemos poner __ a los métodos, para que sólo realicen tareas en la misma clase, nadie accede a ellos
class Persona():
    __nombre = ""#no deja cambiar el nombre con __
    apellido = ""
    __edad = 0
    genero = "sin definir"

    #El constructor se crea con una función __init__(self)
    def __init__(self, nombre, apellido, genero):

        self.__nombre = nombre
        self.apellido = apellido
        self.genero = genero

    def asistente(self):

        return "La persona "+self.__nombre+" está hablando..."
    

    def camina(self):

        return "La persona "+self.__nombre+" está caminando ---->"
    

    def setNombre(self, nombre):
        self.__nombre = nombre

    
    def setEdad(self, edad):
        if edad > 0 or edad < 100:
            self.__edad = edad
        else:
            print("Error en la edad")


    
    #+\para seguir escribiendo abajo
    def getDatos(self):
        
        return "Nombre: "+self.__nombre+" Apellido: "+self.apellido+" Edad: "+str(self.__edad)+\
        " Género: "+self.genero
    

juan = Persona("Juan", "Palantir", "Mascle")

print(juan.asistente())

print(juan.camina())

print(juan.getDatos())

print(juan.__getattribute__)

andre = Persona("Andre", "Anduril", "Femenino")

print(andre.getDatos())

juan.__nombre = "Homero"

print("primer intento de cambiar nombre ----> " + juan.getDatos())

juan.setNombre("Homero")

juan.setEdad(37)

print("Segundo intento de cambiar nombre ----> " +juan.getDatos())
