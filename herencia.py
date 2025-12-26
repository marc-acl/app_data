class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatos(self):

        return "Nombre: " +self.nombre+" Apellido: "+ self.apellido+" Edad: "+str(self.edad)
    
    def habla(self):

        return "Estoy hablando ----> "+self.nombre
    
    def piensa(self):

        return "Estoy pensando ------> "+self.nombre
    
#entre paréntesis se pone la clase de la que hereda
class Estudiante(Persona):
    
    def __init__(self, nombre, apellido, edad, escuela):
        #super().__init__(nombre, apellido, edad)
        Persona.__init__(self, nombre, apellido, edad)
        self.asignatura = []
        self.escuela = escuela
    
    def setAsignatura(self, asignatura):
        self.asignatura.append(asignatura)

    def getAsignaturas(self):
        return self.asignatura
    
    def getDatos(self):
        return super().getDatos() + " Escuela: " + self.escuela
    

class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):
        #super().__init__(nombre, apellido, edad)
        Persona.__init__(self, nombre, apellido, edad)
        self.empresa = empresa

    def trabajaEmpresa(self):
        return "Trabaja en: "+self.empresa
        
    def getDatos(self):
        return super().getDatos()+" Empresa: "+self.empresa
        
#En python existe la herencia multiple. Las clases tienen preferencia según el orden en el que se hereden
#Es decir, la clase más a la izquierda tiene más preferencia. En este caso, trabajador.
#el constructor en init da prioridad a la clase de la que se hereda más a la izquierda
#tenemos que cambiar la palabra super por la clase a la que corresponde la herencia en las clases
#Estudiante y Trabajador, es decir Persona.__init__(self, nombre, apellido, edad) para ambas
class Director(Trabajador, Estudiante):

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus_director):
        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
        self.bonus_director = bonus_director
        

    #como la prioridad la tiene la herencia de trabajador, pone empresa por defecto
    def getDatos(self):
        return super().getDatos()+" Bonus Director: "+str(self.bonus_director)

    
    


    

hera = Persona("Hera", "Greek", 45)
print(hera.habla())
print(hera.getDatos())

prometeo = Estudiante("Prometeo", "Greek", 55, "Meandro")
prometeo.setAsignatura("Mitología Griega")
prometeo.setAsignatura("Historia")
prometeo.setAsignatura("Filosofía")
print(prometeo.piensa())
print(prometeo.getAsignaturas())
print(prometeo.getDatos())

zeus = Director("Zeus", "Greek", 50, "Sky", "Meandro", 8000)
print(zeus.getDatos())

