"""Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un 
método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora."""

class Calculadora():
    def __init__ (self):
        self.num1 = int(input("  Primer número: "))
        self.num2 = int(input("  Segundo número: "))
    def elección(self):
        self.elección = str(input(" ¿Qué operación deseas realizar? (sumar, restar, multiplicar o dividir): "))
        if self.elección == "Sumar" or self.elección == "sumar":
            self.solucion = self.num1 + self.num2 
            print( "La suma de :" + str(self.num1) + " mas la de : " +str(self.num2) + " es igual a: " + str(self.solucion))
        elif self.elección == "Restar" or self.elección == "restar":
            if self.num1 > self.num2:
                self.solucion = self.num1 - self.num2
                print( "La resta de :" + str(self.num1) + " menos : " +str(self.num2) + " es igual a: " + str(self.solucion))
            else:
                print("Esa operación no se puede realizar, sólo números positivos ")
        elif self.elección == "Multiplicar" or self.elección == "multiplicar":
            self.solucion = self.num1 * self.num2
            print("El resultado de multiplicar a :" + str(self.num1) + " por " + str(self.num2) + " es " + str(self.solucion))
        elif self.elección == "Dividir" or self.elección == "dividir":
            try:
                self.solucion = self.num1/self.num2
                print("La división de: " + str(self.num1) + " entre: " + str(self.num2)+ " es : " + str(self.solucion))
            except ZeroDivisionError:
                print("No se puede dividir entre 0, operación erronea")
	        
            


operacion=Calculadora()
operacion.elección()