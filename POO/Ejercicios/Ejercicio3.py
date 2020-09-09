class Persona():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def nombre(self):
        return self.nombre
    def edad(self):
        return self.edad
    def mayor_edad(self):
        if self.edad < 18:
            return "Menor de edad"
        else:
            return "Mayor de edad"
    
Dani=Persona("Dani", 10)
#print(Dani.nombre)
#print(Dani.edad)
#print(Dani.mayor_edad())
print(" El nombre es: " + str(Dani.nombre) + " Con la edad de: " + str(Dani.edad) + " años " + " , por lo tanto es: " + str(Dani.mayor_edad()))
