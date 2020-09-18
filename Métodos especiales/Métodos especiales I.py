#Método __str__()
""" 1º Esté método nos ayuda a que por consola nos devuelva un string con la información
que hemos creado en el constructor de la clase"""

"""class Persona():
    def __init__(self, nombre, ape, edad):
        self.nombre=nombre
        self.apellido=ape
        self.edad=edad
    def __str__(self):
        return "Datos de la persona:\n" + self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.edad)
p1=Persona("Dani", "Diaz", 41)
print(p1)"""



#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

""" 2º Se puede crear un método donde podamos pasarle un número indeterminado de
parámetros.
Para conseguir está acción necesitamos crear en el la zona de parámetros==>
*+nombre del parámetro (ej: *datos)"""

"""class Persona():
    almacen_datos= []
    def __init__(self, *datos):
        for dato in datos:
            self.almacen_datos.append(dato)
       
    def __str__(self):
        return "Datos de la persona:\n" + str(self.almacen_datos[0]) +  "\n" + str(self.almacen_datos [1]) + "\n" + str(self.almacen_datos [2]) 
p1=Persona("Dani", "Diaz", 41)
print(p1)"""

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
""" Para que a la hora de imprimir no tengamos que poner por cada parámetro un self
en el método string, se puede realizar esta forma de poder imprimir por consola 
sin tener que ir enumerrando a cada uno de los elementos de la lista ==> almacen.datos"""
"""class Persona():
    almacen_datos= []
    def __init__(self, *datos):
        for dato in datos:
            self.almacen_datos.append(dato)
        self.getDatos(self.almacen_datos)

    def getDatos(self, info):
        for dato in info:
            print(dato)
       
p1 = Persona("Dani", "Diaz", 41)   
print(p1)"""

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

class Persona():
    almacen_datos= []
    def __init__(self, **datos):
        elementos = datos.items()
        for clave, valor in elementos:
            print(clave, " ", valor)
        
    
       
p1 = Persona(nombre="Dani", Apellido= "Gil", edad=41)   



""" En está ocasión, al poner doble astérisco estamos construyendo un diccionario en
vez de una tupla"""
""" items(), hace devolvernos una lista con una clave valor"""