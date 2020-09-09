"""Desarrollar un programa que cargue los datos 
de un triángulo. Implementar una clase con los 
métodos para inicializar los atributos, 
imprimir el valor del lado con un tamaño mayor 
y  el tipo de triángulo que es 
(equilátero, isósceles o escaleno)."""



class Triangulo():
    def __init__(self):
        self.lado1 = input( "Tamño: ")
        self.lado2 = input( "Tamño: ")
        self.lado3 = input( "Tamño: ")
    def lado1(self):
        return self.lado1
    def lado2(self):
        return self.lado2
    def lado3(self):
        return self.lado3
    def clasificación(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            return "Todos los lados miden lo mismo: " + "Lado1 mide: " + self.lado1 + " Lado2 mide: " + self.lado2 + " Lado3 mide: "  + self.lado3 + " Es Equilátero "
        elif self.lado1 == self.lado2 and self.lado1 != self.lado3:
            return "Lado1 mide: " + self.lado1 + " Es Isosceles "
        elif self.lado2 == self.lado3 and self.lado2 != self.lado1:
            return "Lado2 mide: " + self.lado2 + " Es Isosceles "
        elif self.lado3 == self.lado1 and self.lado3 != self.lado2:
            return "Lado1 mide: " + self.lado1 + " Es Isosceles "
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            return "Todos los lados miden desigual: " + "Lado1 mide: " + self.lado1 + " Lado2 mide: " + self.lado2 + " Lado3 mide: "  + self.lado3 + " Es Escaleno "
        
        
        
#Hay que realizar los condicionales que nos quedan!!!
t=Triangulo()
print(t.lado1)
print(t.lado2)
print(t.lado3)
print(t.clasificación())