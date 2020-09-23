class Cliente():
    cliente =[]
    def __init__(self, nombre, dni, edad):
        self.nombre=nombre
        self.dni = dni
        self.edad=edad
        try:
            if self.edad < 18 or self.edad > 100:
                self.edad = "No permitido para la compra"
                
            else:
                pass
        except:
            print("Revisar datos")
        
    def getdatos(self):
        return "El nombre del comprador es: " + self.nombre.capitalize() + " con dni: " + str(self.dni) + " con edad: " + str(self.edad)
    

class Modelo():
    def __init__(self, marca, serie, fabricacion, precio):
        self.marca = marca
        self.serie = serie
        self.fabricacion = fabricacion
        self.precio = precio
    def getinformacion(self):
        return "la marca del coche es : " + self.marca + " de la serie: " + self.serie + " con año de fab: " + str(self.fabricacion) + " con un precio de: " + str(self.precio)

class venta(Cliente, Modelo):
    venta = []
    def __init__(self, nombre, dni, edad, marca, serie, fabricacion, precio):
        Cliente.__init__(self, nombre, dni, edad)
        self.venta.append(Cliente)
        Modelo.__init__(self, marca, serie, fabricacion, precio)
    def getdatos(self):
        return super().getdatos() + " la marca del coche es : " + self.marca.capitalize() + " de la serie: " + self.serie.capitalize() + " con un precio de: " + str(self.precio)

    def venta(self):
        self.venta.append({"nombre: ": self.nombre, "Marca: ": self.marca, "Serie: ":self.serie, "Precio: ": self.precio})
        return
        
        

cliente1= Cliente("Dani", 7188128, 41)

print(cliente1.getdatos())

#modelo1= Modelo("Ford", "Fiesta", 2009, 1800)
#print(modelo1.getinformacion())

#venta1 = venta("David", 654321, 10, "ford", "sierra", 2019, 1800)
#print(venta1.getdatos())
#print(venta1.venta())


