""" ¿Qué es un constructor?. Un método especial que tiene
todas las clases que le dan un estado inicial a los objetos"""
class Persona():
    nombre=""
    apellido=""
    edad=0
    genero="sin definir"

    def __init__(self, nombre, apellido, edad, genero):  #Este es el constructor con objetos iniciales
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        

        

    def hablar(self):

        return "La persona que se llama " + self.nombre + " esta hablando"

    def caminar(self):

        return "La persona que se llama " + self.nombre + " esta caminando"

    def getdatos(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.edad) + " Género: " + self.genero

p1 = Persona("Pablo ", "Díaz ", 41, "Masculino ")#Tenemos que pasar los 4 parámetros antes fijados en el constructor
p2 = Persona("Alicia", "Marquez", 21, "Femenino")
print(p1.getdatos())

#print(p1.hablar())
#print(p1.caminar())
