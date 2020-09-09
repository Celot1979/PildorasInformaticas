class Cuenta():
    titular={}
    def __init__(self, titular):
        self.titular=titular
        self.cantidad =""
    def setCuenta(self,cantidad):
        self.cantidad=cantidad
        return self.cantidad

    def setTitular(self, titular):
        return "El titular de la cuenta es: " + self.titular   
        
    def setIngresar(self,ingresar):
        self.ingresar = ingresar
        if self.ingresar < 0:
            print("Error en el ingreso")
        else:
            self.cantidad= self.cantidad + self.ingresar
            return "La cantidad ingresada es: " + str(self.ingresar) + " el total en su cuenta es "\
                + str(self.cantidad)

    def setRetirar(self, sacar):
        self.sacar=sacar
        if self.sacar != 0:
            self.cantidad= self.cantidad - self.sacar
            return "Se ha retirado:  " + str(self.sacar) + " en la cuenta queda: " + str(self.cantidad)
        else:
            print("Error debe de ser un número negativo")

    def getDatos(self):
        return "El titular es: " + self.titular + " Ingreso:  " + str(self.ingresar) \
            + " sacó: " + str(self.sacar) + " .El total en su cuenta es: " + str(self.cantidad)





cliente = Cuenta("Daniel")
cliente.setCuenta(50)
cliente.setIngresar(250)
cliente.setRetirar(20)
print(cliente.getDatos())


