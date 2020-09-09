class Persona():
    """2º_nombre=" " Sólo será accesible dentro de la clase, pero no llamar 
    fuera de la clase(sentencias).También podemos usarla en clases 
    heredadas"""
    __nombre= "" #En principio usaremos los dos guiones bajos
    
    """2º__apellido=" " Se encapsula más. Sólo se puede usar 
    dentro de la clase, ni siquiera podría las clases heredadas"""
    
    apellido= ""
    edad=0
    genero="sin definir"

    def __init__(self, nombre, apellido, edad, genero):  #Este es el constructor con objetos iniciales
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        

   #Habría que poner los dos guiones en todas propiedades de los métedos que lleve nombre     

    def hablar(self):

        return "La persona que se llama " + self.__nombre + " esta hablando"

    def caminar(self):

        return "La persona que se llama " + self.__nombre + " esta caminando"

    def getdatos(self):

        return "Nombre: " + self.__nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.edad) + " Género: " + self.genero

p1 = Persona("Pablo ", "Díaz ", 41, "Masculino ")#Tenemos que pasar los 4 parámetros antes fijados en el constructor
p1.nombre= "Alicia" 
""" 1º Al no estar encapsulado, se puede cambiar las propiedades.
Algo que puede pasar desafortunamente ó malintecionadamente cuando
se trabaj en grupo o el usario decide romper la app"""

""" Ahora no le cambiaría el nombre, porqeu el nombre está encapsulado"""
print(p1.getdatos())