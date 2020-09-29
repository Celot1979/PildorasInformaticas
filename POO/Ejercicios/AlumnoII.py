class Alumno():
    cont=0
    alumnos=[]
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.lista_notas = []
    def __str__(self):
        return "El alumno es:  " + self.nombre + " con apellido: " + self.apellido
    def pon_nota (self, nota):
        self.nota = nota
        self.lista_notas.append(self.nota)
        self.cont += 1
        return "Las notas son: " + str(self.lista_notas) + "El número de notas añadidas son: " + str(self.cont)

    def nota_media(self):
        self.suma_notas = sum(self.lista_notas)
        self.media = self.suma_notas/self.cont
        return "El alumno:" + self.nombre + " con apellido: " + self.apellido + " con las notas: " + str(self.lista_notas) + " y una calificación media de: " + str(self.media)

    def __cmp__(self,otro):
        if  isinstance(otro, Alumno):
            if self.nombre == otro.nombre:
                return 0

            elif self.nombre < otro.nombre:
                return -1
                
        else:
            return 1
            

    
             




print("")
A1 = Alumno("Dani", "Gil")
print(A1)
print("")
print(A1.pon_nota(6))
print("")
print(A1.pon_nota(8))
print("")
print(A1.nota_media())

print("")
print("//////////////////////////////////////////////////////////////////////////")
print("")
A2 = Alumno("Pedro", "Diaz")
print(A2)
print("")
print(A2.pon_nota(9))
print("")
print(A2.pon_nota(9))
print("")
print(A2.nota_media())
print("")
print(A1.__cmp__(A2))
