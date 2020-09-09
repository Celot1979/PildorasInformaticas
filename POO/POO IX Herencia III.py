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
        #Se hereda de la clase padre (Persona)
        # 3º Se debe de llamar a la clase Persona y 
        # pasarle un self en el los parametros
        Persona.__init__(self, nombre, apellido, edad)
        self.escuela=escuela #Hay que poner el self/s del nuevo parámetro

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Escuela " + self.escuela
        
    
    def estudiar(self):
        return "Estoy estudiando" 

class Trabajador(Persona):
    def __init__(self,nombre,apellido,edad,empresa):#Se crea constructor 
        #Se hereda de la clase padre (Persona)
        # 2º Se debe de llamar a la clase Persona y 
        # pasarle un self en el los parametros
        Persona.__init__(self, nombre, apellido, edad)
        self.empresa = empresa #Propio método de la clase.
        #Ahora hereda todo el constructor de Persona + propio método

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Empresa: " + self.empresa

    def trabaja(self):
        return "Estoy trabajando"

class Director(Trabajador,Estudiante):
    #Podríamos pensar que para heredar de las dos clases 
    #usariamos el método Super(), pero no es así. 
    # 1º Se realiza así:
    
    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
        self.bonus=bonus
    
    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Bonus: " + str(self.bonus)
    

    def dirige(self):
        return "Estoy dirigiendo"


persona1=Persona("Javier", "Gómez", 41)  
estudiante1=Estudiante("Eva", "Ruíz", 23, "Ins.Carreño") 
print("------------------------------------------")
#print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
print("------------------------------------------")
trabajador1=Trabajador("Pepe", "Ruiz", 23, "C.cam")
print(trabajador1.getDatosPersonales())
print("------------------------------------------")
director1=Director("Lomba","Gomez",54,"lua","San Fernando",1500)
print(director1.getDatosPersonales())
print("------------------------------------------")
#Ahora al imprimir veremso que hereda lo mandado, 
# más los parámetros nuevos