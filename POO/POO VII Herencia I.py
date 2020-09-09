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

        
class Estudiante(Persona): #Clase que hereda

    def estudiar(self):
        return "Estoy estudiando" 


persona1=Persona("Javier", "Gómez", 41)  
estudiante1=Estudiante("Eva", "Ruíz", 23) #Estancia de una clase heredada         

print(persona1.getDatosPersonales())#Imprimir sentencia Super Clase
print(estudiante1.getDatosPersonales())#Imprimir clase que herededa

#Empezaremos el video 37