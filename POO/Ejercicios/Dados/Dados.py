import random
#@Author: Daniel Gil
#@param: Constructor
#@param: Métodos
#@return: Mensajes por consola de las acciones que el programa vaya ejecutando
#@Version. 5.3
class Dados:
    def __init__(self) -> None:
        try:
            self.cantidad = int(input("¿Cuánto dinero quieres depositar en el bote?:\n"))
        except ValueError:
            print("Has introducido letras en vez de números")
        """ En el constructor se ha realizado una prueba con la pregunta de la cantidad de bote que el usuario quiere dejar para jugar.
        Si por alguna razón el usuario quisiera introducir letras en vez números, le saldrá la excepción. """

    def getInformacion(self):
        try:
            return  "La cantidad que va a dejar el jugador de deposito va a ser de : " + str(self.cantidad)
        except AttributeError:
            print("Has introducido letras en vez de números")
        """ El método informa / congirma de la cantidad introducida.
        Si por alguna razón el usuario quisiera introducir letras en vez números, le saldrá la excepción. """
    
    def setApuesta(self):
        self.Apuesta = int(input("¿Qué cantidad quieres apostar?\n"))
        try:
            if self.Apuesta < self.cantidad:
                self.Dinero = self.Apuesta
            else:
                print("No tienes fondos suficientes para jugar esas cantidades")
        except ValueError:
            print("Has cometido un error")
        """ El método se pide al usuario la cantidad que desea apostar.
        En la prueba, siempre que el dinero que se apueste sea menor que la cantidad que quede en el bote, se permite la continuación del programa. """
        

    def setTiradas(self):
        self.verificador = 1
        #Verificador del bucle
        while self.cantidad > 0 and self.verificador == 1:
            print("BIENVENIDO AL JUEGO DE LOS DADOS")
            self.p1= str(input("¿Deseas Jugar?:\n"))
            #Condicional para que el propio usuario decida se desea seguir jugando ó terminar con el juego
            if self.p1 == "si":
                print("Vamos alla !!!!!! ")
                print("Lanza los dados !!!!!")

                self.Dado1 = random.randint(1,6)
                self.Dado2 = random.randint(1,6)
                self.Dado3 = random.randint(1,6)
                print(self.Dado1, self.Dado2, self.Dado3)
                #Tirada aleatorio de las 6 caras de los tres dados en el juego

                

                if self.Dado1 != self.Dado2 and self.Dado1 == self.Dado3:
                    self.cantidad = self.cantidad + (self.Apuesta * 2)
                elif self.Dado1 == self.Dado2 and self.Dado1 != self.Dado3:
                    self.cantidad = self.cantidad + (self.Apuesta * 2)
                elif self.Dado1== self.Dado3 and self.Dado1 != self.Dado2:
                    self.cantidad = self.cantidad + (self.Apuesta * 2)
                elif self.Dado1 == self.Dado3 and self.Dado1 == self.Dado3:
                    self.cantidad = self.cantidad + (self.Apuesta * 3)
                elif self.Dado1 == 6 and self.Dado2 == 6 and self.Dado3 == 6 :
                    self.cantidad = self.cantidad + (self.Dinero * 5)
                else:
                    self.cantidad = self.cantidad - self.Apuesta

                #Posibilidades del juego en cada tirada.
                #En tres se dobla lo juagado. 
                #En una opción se triplica.
                #En una se quintuplica.

                print(self.cantidad)
                self.Apuesta = int(input("¿Qué cantidad quieres apostar?\n"))
                #Al ser un bucle se permite al usuario que continue apostando y tirando de los dados.
                if self.Apuesta > self.cantidad and self.cantidad == 0:
                    print("No tienes suficientes fondos")
                    self.p2 = str(input("¿Quieres recargar el bote para seguir jugando?\n"))
                    if self.p2  == "si":
                        try:
                            self.p3 = int(input("¿Cuánto recargar?\n"))
                            self.cantidad += self.p3
                        except AttributeError:
                            print("HAs introducido caracteres no númericos")
                        
                    elif self.p2 == "no":
                        print("Gracias por jugar con nosotros. Esperamos volver a verte pronto.")
                        self.verificador = 2

                    """ Si el usuario se queda sin efectivo en el bote, se le avisa. Además se le da la posibilidad de poder recargar el bote y seguir jugando """

                    


                
                


                



            elif self.p1 == "no":
                print("Hasta la vista. Gracias por jugar con nosotros")
                self.verificador = 2


        








jugar = Dados()

print(jugar.getInformacion())

jugar.setApuesta()
jugar.setTiradas()
