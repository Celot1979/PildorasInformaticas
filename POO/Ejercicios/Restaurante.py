class Restaurante():
    #Inicimamos clase
    def __init__ (self):
        #Se graban las reservas
        self.reserva =[]
    
        # menu del programa
    def menu(self):
        print()
        menu=[
            ['Programa de Gestión del Restaurante "El Ancla"'],
            ['1. Reserva Teléfonica'],
            ['2. Comprobación de Horario'],
            ['3. Comprobación de Disponibilidad de mesas'],
            ['4. Buscar Reserva'],
            ['5. Editar Reserva'],
            ['6. Borrar Reserva'],
            ['7. Salir del programa'],
        ]

        for x in range(8):
            print(menu[x][0])

        opcion=int(input("Introduzca la opción deseada: "))
        if opcion == 1:
            self.add()
        elif opcion == 2:
            self.comprobar()
        elif opcion == 3:
            print("En construcción")
        elif opcion == 4:
            print("En construcción")
        elif opcion == 5:
            print("En construcción")
        elif opcion == 6:
            print("En construcción")
        elif opcion == 7:
            print("Saliendo del programa...")
            exit()
        self.menu()

    def add (self):
        print("---------------------")
        print(" AÑADIR RESERVA ")
        print("---------------------")
        nombre = str(input("Introduzca el nombre: "))
        apellido= str(input("Introduzca el Apellido: "))
        
        telf= str(input("Introduzca el número de teléfono: "))
        email= str(input("Introduccir dirección de E-mail: "))
        self.reserva.append({"nombre: ": nombre, "Apellido: ": apellido, "telf":telf, "email": email})
        print(self.reserva)
    def comprobar(self):
        print("--------------------------------------------")
        print(" COMPROBAR EL HORARIO DE LA RESERVA ")
        print("--------------------------------------------")
        mesas=10
        cita = int(input("Hora de la reserva: "))
        if cita > 1300 and cita < 1600:
            print("Reserva")
        else:
            print("No reserva")
        
            



        

        




        

c=Restaurante()
c.menu()
