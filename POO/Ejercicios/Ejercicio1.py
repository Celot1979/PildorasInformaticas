class Alumno():
    def __init__(self, nombre):
        self.nombre= nombre
        
    def nombre(self):
        return self.nombre
    
    def evaluar(self, nota):
        self.nota = nota
        if self.nota <5:
            return "Suspenso"
        elif self.nota == 6:
            return "Bien"
        elif self.nota == 7 or self.nota == 8:
            return "Notable"
        elif self.nota == 9 or self.nota == 10:
            return "Sobresaliente"
      

    def final(self):
        return "El alumno: " + self.nombre + " ha tenido una nota de: " + str(self.nota) + " .Tiene una calificación de: " + self.evaluar(10)
           
alumno1= Alumno("George")
print(alumno1.nombre)

print(alumno1.evaluar(7))
print(alumno1.final())



"""Realizar un programa que conste de una clase 
llamada Alumno que tenga como atributos el nombre
 y la nota del alumno. Definir los métodos para 
 inicializar sus atributos, imprimirlos y mostrar 
 un mensaje con el resultado de la nota y si ha 
 aprobado o no."""

