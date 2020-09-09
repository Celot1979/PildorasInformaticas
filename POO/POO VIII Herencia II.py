class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad = edad

    def getDatosPersonales(self):
        return "nombre: " + self.nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.edad)

    def habla(self):
        return "Estoy hablando"

    def piensa(self):
        return "Estoy pensando" 
    
    def camina(self):
        return "Estoy camina"

    def come(self):
        return "Estoy comiendo"

        
class Estudiante(Persona):#Método heredado de la clase Persona 
    def __init__(self, nombre, apellido, edad, escuela):
        super().__init__(nombre, apellido, edad)
        self.escuela=escuela #Hay que poner el self/s del nuevo parámetro

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Escuela " + self.escuela
        
    
    def estudiar(self):
        return "Estoy estudiando" 


persona1=Persona("Javier", "Gómez", 41)  
estudiante1=Estudiante("Eva", "Ruíz", 23, "Ins.Carreño") 

#print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())

""" La instrucción super()sirve para que una clase 
hija herede de la clase padre el constructor, y además
pueda añadir sus propias propiedades

La instrucción super() llama a la clase padre (init en este caso)
"""
""" ATENCIÓN : En la clase de gdatospersonales de estudiantes,
es un método heredado de la clase Persona"""