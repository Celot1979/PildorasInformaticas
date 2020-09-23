class Persona():
    
    __nombre= "" 
    apellido= ""
    __edad=0 #1º Protegemos la edad con dos guiones
    genero="sin definir"

    def __init__(self, nombre, apellido, genero):  #2º Quitamos la edad del constructor, pues
        #haremos un método especial
        self.__nombre = nombre
        self.apellido = apellido
        
        self.genero = genero
        

    def setEdad(self, laEdad): #Esto es un método de acceso
        if laEdad < 0 or laEdad > 100:
            print("Error en la edad") 
        else:
            self.__edad = laEdad #Al ser la edad correcta,
            # hacemos que se almacene en la propiedad edad (self.__edad)
            return self.__edad

    def hablar(self):

        return "La persona que se llama " + self.__nombre + " esta hablando"

    def caminar(self):

        return "La persona que se llama " + self.__nombre + " esta caminando"

    def getdatos(self):# Esto sería un Getter. Nos da toda la información
        # de todas las propiedad ( incluida edad), pero otro método no podría
        #darnos edad.

        return "Nombre: " + self.__nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.__edad) + " Género: " + self.genero

p1 = Persona("Pablo ", "Díaz ",  "Masculino ") 
p1.setEdad(13) #Es totalmente necesario poder llamar al método de acceso
#Luego de escribe la sentencia de p1.getdatos()
print(p1.getdatos())

""" La encapsulación además de permitinos proteger 
ciertas partes del código de acesos externos, es decir
a nuestro programa como y de qué manera se almacena una
propiedad (eje: edad) en este ejemplo.

Los métodos de acceso consite en impedir al acceso directo a la propiedad desde
fuera, pero si permitir el acceso mediante un FILTRO que regulará o
describirá el rango de valores que nsosotros decidimos que va usar
el usario
Existen dos métedos de accesos:
Setters ==> set Almacenaría un valor en propiedades(un rango 
que nosotros decidamos)
Getters ==> get Accede al valor de esa propiedad.
"""
