from random import randint
class Administrativo():
    def __init__(self,apellido1, apellido2, nombre, fecha):
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.nombre=nombre
        self.fecha=fecha
    def sueldo(self):
       self.sueldo = 1200
       return "El sueldo es de " + str(self.sueldo)
    def __str__(self):
        return "El primer apellido es: " + self.apellido1 + "\n" + "El segundo apellido es: " + self.apellido2 + "\n" + "El nombre es: " + self.nombre + "\n" + "Fecha de ingreso: " + self.fecha 

    def usuario(self):
        return "adm + " + self.nombre[0] + self.apellido1

    def passw(self):
        self.aleatorio = randint(1000,4000)
        return self.aleatorio

class Docente(Administrativo):
    def __init__(self, nombre, apellido, edad, escuela):
        super().__init__(nombre, apellido, edad, escuela)
        

    def tar (self, hora, tariafa):
        self.hora = hora
        self.tariafa=tariafa
        return str(self.hora * self.tariafa)
    def __str__(self):
        return "El primer apellido es: " + self.apellido1 + "\n" + "El segundo apellido es: " + self.apellido2 + "\n" + "El nombre es: " + self.nombre + "\n" + "Fecha de ingreso: " + self.fecha 

    def usuario(self):
        return "doc + " + self.nombre[0] + self.apellido1 

    def passw(self):
        return super().passw()







personal = Administrativo("Gil", "Martinez", "Daniel", "22 de Agosto de 2010")
Docente1=Docente("Fernandez", "Gil", "Elisa", "25 de Mayo 2006")
print(personal)
print(personal.sueldo())
print(Docente1)
print(Docente1.tar(3,5))
print(Docente1.usuario())

print(Docente1.passw())



