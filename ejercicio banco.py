#Se trata de crear una clase que construya cuentas corrientes bancarias. Para ello deberás: 
#• Crear una clase con el nombre de CuentaCorriente con tres atributos que serán: 
#o El nº de la cuenta (un string numérico con el nº de cifras que quieras) 
#o El titular de la cuenta 
#o El saldo de la cuenta 
#• Crear un método getter que nos muestre la información de la cuenta. Debe 
#mostrarnos el nº, el titular y el saldo. 
#• Crear un método que nos permita ingresar dinero en la cuenta 
#• Crear un método que nos permita retirar dinero de la cuenta 
#Prueba el programa creando un objeto de tipo CuentaCorriente, ingresa y retira dinero de la 
#cuenta y finalmente muestra los datos de la cuenta. 


class CuentaCorriente():
    #numero_cuenta = ""
    #titular = ""
    #saldo = 0
    #no es necesario crear estas variables

    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):
        return "Número de cuenta: "+self.numero_cuenta+" Titular: "+self.titular+" Saldo: "+str(self.saldo)
    
    def setDinero(self, saldo):
            self.saldo += saldo

    def getDinero(self, retiro):
         if self.saldo >= retiro:
              self.saldo -= retiro
              return "RETIRADO: "+str(retiro)
         else:
              return "SALDO INSUFICIENTE"
         

class CuentaJoven(CuentaCorriente):
     
    def __init__(self, numero_cuenta, titular, saldo, bonus):
        super().__init__(numero_cuenta, titular, saldo)
        self.bonus = bonus
        self.saldo = saldo+bonus

    def getBonus(self):
         return "El bonus es de: "+str(self.bonus)
    
    def getDatos(self):
         return super().getDatos()+" el bonus es de: "+str(self.bonus)

     
     
         

andres = CuentaCorriente("52364", "Andres Londoño", 5800)
print(andres.getDatos())
andres.setDinero(2000)
print(andres.getDatos())
andres.getDinero(250)
print(andres.getDatos())

maria = CuentaCorriente("785423", "María Saavedra", 9560.36)
print(maria.getDatos())
maria.setDinero(7500)
print(maria.getDatos())
maria.getDinero(750)
print(maria.getDatos())

diana = CuentaJoven("999148", "Marcela Arias", 28000, 300)
print(diana.getDatos())
diana.setDinero(3000)
print(diana.getDatos())
diana.getDinero(700)
print(diana.getDatos())