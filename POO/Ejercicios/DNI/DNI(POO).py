""" Haz una clase llamada Persona que siga las siguientes condiciones:

Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo. Si quieres añadir algún atributo puedes hacerlo.
Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo (0 números, cadena vacía para String, etc.). Sexo sera hombre por defecto, usa una constante para ello.
Se implantaran varios constructores:

-Un constructor por defecto.
-Un constructor con el nombre, edad y sexo, el resto por defecto.
-Un constructor con todos los atributos como parámetro.

Los métodos que se implementaran son:
*calcularIMC(): calculara si la persona esta en su peso ideal (peso en kg/(altura^2  en m)), si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos), significa que esta por debajo de su peso ideal la función devuelve un 0  y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un 1. Te recomiendo que uses constantes para devolver estos valores.
*esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
*comprobarSexo(char sexo): comprueba que el sexo introducido es correcto. Si no es correcto, sera H. No sera visible al exterior.
*toString(): devuelve toda la información del objeto.
*generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este su número su letra correspondiente. Este método sera invocado cuando se construya el objeto. Puedes dividir el método para que te sea más fácil. No será visible al exterior.

Métodos set de cada parámetro, excepto de DNI.



Ahora, crea una clase ejecutable que haga lo siguiente:

Pide por teclado el nombre, la edad, sexo, peso y altura.
Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
Para cada objeto, deberá comprobar si esta en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
Indicar para cada objeto si es mayor de edad.
Por último, mostrar la información de cada objeto.
Puedes usar métodos en la clase ejecutable, para que os sea mas fácil. """
import random
import string



class Persona():
    def __init__(self):
        self.nombre = input("Nombre: ")
        self. edad= input("Edad: ")
        self.sexo = input("Sexo")
        if self.sexo  != " ":
            self.sexo = "H"
        else:
            self.sexo = "M"
    def Peso(self):
        self.peso= input( "El peso: ")
   
    def Altura(self):
        self.altura= input("La altura: ")
    """def getAltura(self):
        print("La altura es de :" + self.altura + " cm ")"""
    def dni (self):
        self.dni = input("DNI ")
        if self.dni != " ":
            self.dni = random.randint(0, 999999999)
        else:
            self.dni = dni
    def letra(self):
        self.letra = input("letra")
        if self.letra != " ":
            self.letra = random.choice(string.ascii_letters)
        else:
            self.letra = letra
    
    def getDatos(self):
        print("El nombre es " +  self.nombre + " tiene una edad de " + str(self.edad )+ " su sexo es " + self.sexo  +
        " El DNI es " + str(self.dni) + str(self.letra) + "La altura es de :" + str(self.altura) + " cm" + " El peso es de : " + str(self.peso) + " Kg ")

p1= Persona()
p1.Peso()
p1.Altura()
#p1.getAltura()
p1.dni()
p1.letra()
p1.getDatos()
""" Definir después unos métodos que digan si es mayor de edad y si está gordo o no"""