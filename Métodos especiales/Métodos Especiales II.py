import datetime #Importamos esté módulo para poder mostrar en el 2º ejemplo lo
#la diferencia entre el método __str__ y __repr__

# Método Especial __repr__()
""" Este método es muy parecido - por no decir igual - al método __str__()

Pero la diferencia es que es inequivoco, es decir, es más descriptivo con 
el objeto en la clase. Esa sútil diferencia lo podremos comprobar mejor
en el segundo ejemplo.

Se dice que str es para lenguaje humano, y repr para desarrollo"""
# 1º Ejemplo
"""class Persona():
    def __init__(self, nom, ape, edad):
        self.nombre = nom
        self.apellido = ape
        self.edad = edad

    def __repr__(self):
        return "Datos de la persona:\n" + self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.edad) 


p1 = Persona("Dani", "Gil", 41)
print(p1)"""
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
# 2º Ejemplo
hoy = datetime.date.today() #Almecenamos en está variable la fecha actual
print(str(hoy))
print(repr(hoy))
#Si nos fijamos al imprimir por consola, veremos que la información con repr es
#mucho más precisa
