
class Clientes():
    cliente=[]
    def __init__ (self):
        self.nombre = str(input("¿Cúal es el nombre?: "))
        self.cliente.append(self.nombre)

        self.edad = input("¿Cúal es tu edad?: ")
        try:
            if self.edad < 18 or self.edad > 70:
                print("No es posible vender el auto")
                self.cliente.append("No se puede realizar la transanción")
                
            else:
                self.cliente.append(self.edad)
        except:
            print("Revisar la edad introduccida")


        self.dni = str(input("¿Cuál es tu DNI:? "))
        try:
            if len(self.dni) < 9:
                self.cliente.append(self.dni)
                #print(self.cliente)
            else:
                print("Error")
        except:
            print(" Algo ha salido mal")
            
    def __str__(self):
        return "El comprador " + self.nombre.capitalize() + " con la edad de " + str(self.edad) + " con DNI " + str(self.dni) 
        
class Modelos():
    modelos=[]
    def __init__(self):
        self.marca = str(input("Modelo del vehículo: "))
        self.modelos.append(self.marca)

        self.fabricacion = int(input("Año de fabricación: "))
        try:
            if self.fabricacion > 2000:
                self.modelos.append(self.fabricacion)
                pass
            else:
                print("No tenemos vehículos con más antguedad")
        except:
            print("REVISE LOS DATOS INTRODUCCIDOS")

        self.serie = str(input("¿Serie? : "))
        self.modelos.append(self.serie)

        self.precio = int(input("¿Qué precio tiene?: "))
        try:
            if self.precio <= 0:
                print("Error en el precio")
            else:
                self.modelos.append(self.precio)
        except:
            print("Algo ha pasado.... revisa")
    
    def __str__(self):
        return "El vehículo es de la marca: " + self.marca.capitalize() + " con fecha de fabricación:  " + str(self.fabricacion) + " de la serie:  " + str(self.serie) + " con un precio de: " + str(self.precio)



cliente1 = Clientes()
print(cliente1)

modelo1= Modelos()
print(modelo1)

venta1 = Ventas("Dani", 41, 2345)
print(venta1)

