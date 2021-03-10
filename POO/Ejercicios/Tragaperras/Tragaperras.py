import random
class Tragaperras:
    def __init__(self) -> None:
        self.cantidad = int (input ("Cantidad que desea depositar\n"))   
    def getCantidad(self):
        try:
            if self.cantidad > 50:
                print("Cantidad incorrecta")
            elif self.cantidad < 1:
                print("Cantidad incorrecta")
            else:
                print("El usuario ha ingresado " + str(self.cantidad))
        except IndexError:
            print("En número de mes debe ir entre 1 y 50")
    def setcombinacion(self):
        self.caja1 = random.choice("Manzana Naranja Fresa Cereza Limón Sandía".split())
        #print(self.caja1)
        self.caja2 = random.choice("Manzana Naranja Fresa Cereza Limón Sandía".split())
        #print(self.caja2)
        self.caja3 = random.choice("Manzana Naranja Fresa Cereza Limón Sandía".split())
        print("La combinacion que ha salido es: " + self.caja1 + " - "+ self.caja2 + " - "+ self.caja3)
        
    def getCombinacion(self):
        if self.caja1 != self.caja2 and self.caja2 != self.caja3 or self.caja1 != self.caja3:
            self.cantidad = self.cantidad - 0.50
            print(self.cantidad)
        elif self.caja1 == "Cereza" and self.caja2 == "Cereza"  and self.caja3 == "Cereza":
            self.cantidad = self.cantidad + 30
            print(self.cantidad)
        elif self.caja1 == "Sandía" and self.caja2 == "Sandía"  and self.caja3 == "Sandía":
            self.cantidad = self.cantidad + 20
            print(self.cantidad)
        elif self.caja1 == "Manzana" and self.caja2 == "Manzana"  and self.caja3 == "Manzana":
            self.cantidad = self.cantidad + 5
            print(self.cantidad)
        elif self.caja1 == "Naranja" and self.caja2 == "Naranja"  and self.caja3 == "Naranja":
            self.cantidad = self.cantidad + 5
            print(self.cantidad)
        elif self.caja1 == "Fresa" and self.caja2 == "Fresa"  and self.caja3 == "Fresa":
            self.cantidad = self.cantidad + 5
            print(self.cantidad)
        elif self.caja1 == "Limón" and self.caja2 == "Limón"  and self.caja3 == "Limón":
            self.cantidad = self.cantidad + 5
            print(self.cantidad)
        self.validar =1

    def getCombinacion_Corta(self):
        if self.caja1 == "Cereza" and self.caja2 == "Cereza" and self.caja3 != "Cereza":
            self.cantidad = self.cantidad + 3
            print(self.cantidad)
        elif self.caja1 == "Cereza" and self.caja3 == "Cereza" and self.caja2 != "Cereza":
            self.cantidad = self.cantidad + 3
            print(self.cantidad)
        elif self.caja2 == "Cereza" and self.caja3 == "Cereza" and self.caja1 != "Cereza":
            self.cantidad = self.cantidad + 3
            print(self.cantidad)
        elif self.caja1 == "Sandía" and self.caja2 == "Sandía" and self.caja3 != "Sandía":
            self.cantidad = self.cantidad + 2
            print(self.cantidad)
        elif self.caja1 == "Sandía" and self.caja3 == "Sandía" and self.caja2 != "Sandía":
            self.cantidad = self.cantidad + 2
            print(self.cantidad)
        elif self.caja2 == "Sandía" and self.caja3 == "Sandía" and self.caja1 != "Sandía":
            self.cantidad = self.cantidad + 2
            print(self.cantidad)
        elif self.caja1 == self.caja2  and self.caja1 != self.caja3:
            self.cantidad = self.cantidad + 1
            print(self.cantidad)
        elif self.caja1 == self.caja3 and self.caja1 != self.caja2:
            self.cantidad = self.cantidad + 1
            print(self.cantidad)
        elif self.caja1 != self.caja2 and self.caja2 != self.caja3 or self.caja1 != self.caja3:
            self.cantidad = self.cantidad - 0.50
        self.validar = 2


    def setPartida(self):
        self.getCantidad()
        while self.cantidad > 0:
            opcion = str(input("Deseas seguir jugando:\n1.si\n2.no\n==>"))
            if opcion == "si":
                self.setcombinacion()
                self.getCombinacion()
                self.getCombinacion_Corta()
            elif opcion == "no":
                print("Gracias por su visita")
                break

  



        


        
        
        
        



Jugador = Tragaperras()
Jugador.setPartida()

""" Falla cuando son 2 iguales. """