import random
import time
import os
""" Tenemos funciones acotadas / empaquetadas para que hagan un trabajo especifico
Revisar las llamdas a los métodos para depurar errores y mejorar el mensaje por código """
class Memoria:
    def __init__(self) -> None:
        os.system("clear")
        print("C O M I E N Z A  E L   J U E G O !!!!!.")
        time.sleep(3)
        os.system("clear")
        print("P R E P A R A  T U  M E N T E  !!!!!.")
        time.sleep(2)
        os.system("clear")
        try:
            self.dificultad = int (input("Modos de Juego:\n1.Fácil\n2.Medio\n3.Dificil\n==>"))
            if self.dificultad == 1 or self.dificultad == 2 or self.dificultad == 3:#En cada una de las dificultades, va decreciendo el tiempo de memorización.
                if self.dificultad == 1:
                    self.tiempo = 5
                elif self.dificultad == 2:
                    self.tiempo = 3
                elif self.dificultad == 3:
                    self.tiempo = 2

                print("Continuemos en el juego")
            else:
                print("Lamentablemente esa eleccion no está dentro de las opciones del juego")
            
        except ValueError:
            print("Lamentablemente esa eleccion no está dentro de las opciones del juego")
        """ Creamo un constructor donde el usuario podrá elegir el nivel de dificultad. Dependiendo de la misma, el tiempo de borrado en consola de la serie
        se irá acortando.
        Adicionalmente se realiza una evaluación de lo introduccido por el usuario, si no está dentro de los parámetros se sale del programa """
        
    def getDificultad(self):
        if self.dificultad == 1:
            self.eleccion = "Fácil"
        elif self.dificultad == 2:
            self.eleccion = "Medio"
        if self.dificultad == 3:
            self.eleccion = "Dificil"

        print("La dificultad elegida por el jugador es: " + self.eleccion)

        """ Este getter tiene como misión informar al usuario de la elección que a efectuado. A posteriori daremos una opción de modificar la elección. """



    def setPrograma (self, p):#Realiza número aleatorios y los agrega a una lista
        self.lista_programa=[]
        for i in range(p):
            self.serie = random.randint(1,3)
            self.lista_programa.append(self.serie)

    def getPrograma(self):#Pasa por consola la información de la lista aleatoria del sistema.Con una función de borrado de contenido de la consola
        def borrado ():
            time.sleep(self.tiempo)
            os.system("clear")
        print(self.lista_programa)
        borrado()
        

    def setUsuario (self,u):#Petición de introduccir al usuario los digitos memorizados y los agrega a una lista
        self.lista_Usuario=[]
        try:
            for i in range (u):
                self.user = int(input("Introduce uno a uno los digitos que has memorizado de la serie que has visto: "))
                self.lista_Usuario.append(self.user)
        except ValueError:
            print("1º Introduce un número + Enter.\n2º Sólo se puede introduccir digitos.")
        
    def getUsuario(self):#Pasa por consola la información de la lista del usuario.Con una función de borrado de contenido de la consola
        def borrado ():
            time.sleep(self.tiempo)
            os.system("clear")
        print(self.lista_Usuario)
        borrado()

    def setComparar(self):#Compara una lista con la otra buscando que sean iguales. Si lo son arroja el mensaje de correcto o no.
        self.t = 0
        for l in range(len(self.lista_programa)):
            if self.lista_programa == self.lista_Usuario:
                print("Correcto")
                
            else:
                print("Incorrecto")
                print("Has terminado el juego. Para volver a empezar debes de comenzar nuevamente")
                time.sleep(self.tiempo)
                os.system("clear")
                self.t = 10#Si es incorrecto pasará al valor 10 en la funcion rondas. Eso hará que rompa el while y se termine el juego.
                break
                
                    
    def setRondas(self):#Función creada para gestionar las rondas
        self.t = 0
        i = 0
        
        while self.t < 10:
            self.setPrograma(i)
            self.getPrograma()
            self.setUsuario(i)
            self.getUsuario()
            self.setComparar()
            i += 1
            self.t += 1
            
           
            
        

                
        
    
    







j = Memoria()
j.getDificultad()
j.setRondas()






