class Reserva():
    reserva=[]
    def __init__(self,nombre, apellido, telefono, email):
        self.nombre = str(input("Cual es el nombre del titular de la reserva: "))
        self.apellido = str(input("Primer apellido: "))
        self.teléfono = int(input("Número de teléfono: "))
        self.email = str(input("Dirección de E-mail: "))
        self.reserva.append({"Nombre" : nombre.capitalize(), "Apellido" : apellido, "telefono": telefono.isdigit(), "E-mail:" : email})
        print(self.reserva)
    def setBuscar(self):
        nombre= input("Introduzca el nombre del contacto: ")
        for x in range(len(self.reserva)):
            if nombre == self.reserva[x]["Nombre"]:
                print("Datos de la reserva:")
                print("Nombre: ", self.reserva[x]["nombre"])
                print("Teléfono: ", self.reserva[x]["telf"])
                print("E-mail: ", self.reservas[x]["email"])
                return x
	
        
    def setFranja_horaria_comida(self,franja):
        self.franja= int(input("Determina la hora de la reserva: "))
        if self.franja > 1300 and self.franja < 1600:
            print("La reserva es posible")

        else:
            print("Esta fuera de hora")
           

    





cliente1 = Reserva("Dani", "Gil", "686059341", "zata@hotmail.com")
cliente1.setFranja_horaria_comida(1200)


#print(cliente1)