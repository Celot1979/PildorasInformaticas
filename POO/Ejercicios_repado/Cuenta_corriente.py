import sys
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
            
num = str(input("Numero de la cuenta es: "))
nombre = str(input("Nombre del titular: "))
cantidad = int(input("Cantidad:"))
opcion = int(input("¿Qué opción te interesa " + "\n" + "1.Salir"+ "\n" + "2.Ingresar" + "\n" + "3.Retirar"))
if opcion == 1:
    print("Muchas gracias por su visita")
    sys.exit()

cuenta = Cuenta(num,nombre,cantidad)

if opcion == 2:
   dir = int(input("Cantidad a ingresar :"))
   cuenta.ingresar(dir)
if opcion == 3:
   dir = int(input("Cantidad a retirar :"))
   cuenta.retirar(dir)

print(cuenta.getDatos())




