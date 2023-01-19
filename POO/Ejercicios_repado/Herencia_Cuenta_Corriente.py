class Cuenta():
    def __init__(self, numero, titular,saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def getDatos(self):
        return "El número de la cuenta es " + str(self.numero) + " el titular es " + str(self.titular) + " y la cantidad en su cuenta actualmente es " + str(self.saldo) 
    def ingresar (self,dinero):
        self.dinero = dinero
        if self.saldo == 0:
            self.saldo = self.dinero
        elif self.saldo > 0:
            self.saldo = self.saldo + self.dinero
    def retirar(self,dinero):
        self.dinero = dinero
        if self.saldo < self.dinero:
            print ("No exite suficiente cantidad en su cuenta para retirar " + str(self.saldo))
            sys.exit()
        elif self.saldo > 0:
            self.saldo = self.saldo - self.dinero
            
class Cliente_Joven(Cuenta):
    def __init__(self,numero, titular,saldo,bonus_promocion =0):
        super().__init__(numero, titular, saldo)
        self.bonus_promocion = bonus_promocion
        self.saldo += bonus_promocion

    def getBonusPromocion(self):
        return "El bonnus es " + self.bonus_promocion

    def ingresar (self,ingreso):
        super().ingresar(ingreso)

    def retirar(self,cantidad):
        super().retirar(cantidad)

    def getDatos(self):
        return super().getDatos() + " El bonus  " + str(self.bonus_promocion)
Adulto = Cuenta(1234,"Pedro",5000)
print(Adulto.getDatos())
joven = Cliente_Joven(225825,"Pedro",4500,300)
print(joven.getDatos())