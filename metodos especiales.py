import datetime

class Persona():

    def __init__(self, nombre, apellido, edad):
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        #funciona como el toString
        return "Datos: \n"+self.nombre+"\nApellido: "+self.apellido+" \nEdad:"+str(self.edad)
    
persona1 = Persona("Diana", "Arias Claros", 35)
print(persona1)


class Individuo():

    datos = []
    datos1= []

    #*hace que pueda recibir un número indefinido de parámetros. Datos hace la función de Tupla
    #probamos varias formas 
    def __init__(self, *datos):

        self.datos1 = datos
        print(str(self.datos1)+"*****************")

        for i in datos:
            self.datos.append(i)

        self.getData(self.datos)
        print("Hola")

        self.getData(self.datos1)
        print("*****************")

     
    def getDatos(self):
        
        for i in self.datos:
            return "Datos: " + str(self.datos)
        
        
    def getData(self, info):

        for i in info:
            print(i)#con la i imprime uno en cada línea
    

    def getDatos1(self):
        return "Datos: "+str(self.datos)#así imprime la lista
    

    #def __str__(self):
        #funciona como el toString
        #return "Datos: \n"+self.datos[0]+"\nApellido: "+self.datos[1]+" \nEdad:"+self.datos[3]
    
    #funciona igual al __str__
    def  __repr__(self):
        #funciona como el toString
        return "Datos: \nNombrre: "+self.datos[0]+"\nApellido: "+self.datos[1]+" \nEdad:"+self.datos[3]
    
individuo1 = Individuo("Marcela", "Arias Claros", 35, "Python")
print(individuo1.getDatos())
print("-------------------------------------------------")
print("-------------------------------------------------")
print(individuo1)
print("-------------------------------------------------")
print("-------------------------------------------------")
print(individuo1.getDatos1())


#cuando pongo dos asteríscos, usa un diccionario 

class Avatar():

    datos = []

    def __init__(self, **datos):
       
       self.datos = datos
       print(str(self.datos)+"*************")

       elementos = datos.items()
       
       for i, j in elementos:
           print(i, ": ", j)
        
       


avatar = Avatar(Nombre="Diana", Apellido="Arias", Edad=36)



#Más métodos
print("-------------------------------------------------")
print("-------------------------------------------------")

hoy = datetime.date.today()

print(hoy)
print(str(hoy))
print(repr(hoy))


#Método
print("-------------------------------------------------")
print("-------------------------------------------------")

class Agenda():

    def __init__(self):
        
        self.agenda = {}

    def setContacto(self, nombre, telefono):

        self.agenda[nombre] = telefono

    def __len__(self):

        #si lo imprimimos bajo una instancia de la clase no funciona con diccionarios pero sí con listas y tuplas
        #por eso se sobreescribe desde la clase

        return len(self.agenda)
    

    def getDatos(self):
        
        return self.agenda
    

    def getData(self):

        for key, value in self.agenda.items():
            print(f"Nombre: {key}, Teléfono: {value}")
    
contacto = Agenda()

contacto.setContacto("Diana", "85412369")
contacto.setContacto("María", "2569841")
contacto.setContacto("Marcela", "123789")
contacto.setContacto("Luz", "65412387")

print(len(contacto))
print(contacto.getDatos())
print(contacto.getData())


