class Persona():
    nombre=""
    apellido=""
    edad=0
    genero="sin definir"

    def hablar(self):

        return "La persona que se llama " + self.nombre + " esta hablando"

    def caminar(self):

        return "La persona que se llama " + self.nombre + " esta caminando"

    def getdatos(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.edad) + " Género: " + self.genero

"""La barra invertida después de un espacio en una concatenamiento 
sirve para que en la impresión salga sola una línea y 
no tengamos que escribir  tanto a la derecha"""
p1=Persona()
p1.nombre= "Pablo"
p1.apellido= "Díaz"

#p1.hablar()
#p1.caminar()
print(p1.getdatos())
