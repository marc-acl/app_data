#1.
class Persona():
    def hablar(self):
        return "Persona habla"
    
class Trabajador(Persona):
    def hablar(self):
        return "Trabajador habla"
    
class Director(Trabajador):
    def hablar(self):
        return "Director habla"
    
def personaHabla(lista):

    for persona in lista:
        print(persona.hablar())
    
persona = Persona()
print(persona.hablar())

trabajador = Trabajador()
print(trabajador.hablar())

director = Director()
print(director.hablar())

print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")

listaPersonas = [persona, trabajador, director]
personaHabla(listaPersonas)