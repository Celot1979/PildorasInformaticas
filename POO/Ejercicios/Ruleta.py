import random
#@Author: Daniel Gil
#@param: Constructor
#@param: Métodos
#@return: Mensajes por consola de las acciones que el programa vaya ejecutando
#@Version: 7.0
class Ruleta:
    def __init__(self, nu, co):
        self.numero = nu
        self.color= co
        self.combinacion = str(self.numero) + " " +  self.color
    def getApuesta(self):
        return "El jugador apusta al: " + self.combinacion 

    def setJugada(self):
        self.eleccion = 1
        self.cantidad = 1000
        while self.eleccion ==1:

            self.numero = int(input("Que numero escoges: "))
            if self.numero < 20:
                self.color = str(input("Qué color escoges: "))
                if self.color == "Rojo" or self.color == "Negro":
                    self.apuesta = int(input("Qué cantidad deseas apostar?:\n"))
                    if self.apuesta > 0:
                        self.Ruleta_Numero = random.randint(1,20)
                        self.Ruleta_Color = random.choice(["rojo", "negro"])
                        self.jugada = str(self.Ruleta_Numero) + " " +  self.Ruleta_Color
                        print(self.jugada)
                        if self.jugada != self.combinacion:
                            self.cantidad = self.cantidad - self.apuesta
                            print(self.cantidad)
                        if self.cantidad == 0:
                            print("Lo lamentamos pero no tienes más fondos para seguir jugando")
                            break
                        elif self.jugada == self.combinacion:
                            self.combinacion = self.cantidad + (self.apuesta * 2)
                            print(self.cantidad)

                        op = str(input("Quieres seguir jugando :\n"))
                        if op == "si":
                            continue
                        elif op == "no":
                            print("Muchas gracias por tu vsita. te esperamos pronto.")
                            self.eleccion = 2
                    else:
                        print("No se pueden apostar cuantias negativas")
                        self.eleccion = 2
                    

            else:
                print("El numero debe de ser de entre 1 al 20\nLos colores sólo pueden ser ROJO  O  NEGRO")


                break
            
            
            
           

            

            """self.apuesta = int(input("Qué cantidad deseas apostar?:\n"))
            self.Ruleta_Numero = random.randint(1,20)
            self.Ruleta_Color = random.choice(["rojo", "negro"])
            self.jugada = str(self.Ruleta_Numero) + " " +  self.Ruleta_Color
            print(self.jugada)
            
            if self.jugada != self.combinacion:
                self.cantidad = self.cantidad - self.apuesta
                print(self.cantidad)
                if self.cantidad == 0:
                    print("Lo lamentamos pero no tienes más fondos para seguir jugando")
                    break
            elif self.jugada == self.combinacion:
                self.combinacion = self.cantidad + (self.apuesta * 2)
                print(self.cantidad)

            op = str(input("Quieres seguir jugando :\n"))
            if op == "si":
                continue
            elif op == "no":
                print("Muchas gracias por tu vsita. te esperamos pronto.")
                self.eleccion = 2"""
        
        

    




Ejemplo = Ruleta(12,"Rojo")
print(Ejemplo.getApuesta())
Ejemplo.setJugada()

