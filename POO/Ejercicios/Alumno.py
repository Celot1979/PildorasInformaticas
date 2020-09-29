class Alumno():
    lista=[]
    count=0
    def  __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    def pon_nota(self, nota):
        self.nota=nota
        self.lista.append(self.nota)
        self.count += 1

    def nota_media (self):
        self.suma_notas= sum(self.lista)
        self.media = self.suma_notas/self.count
        return self.media
    def cmp_nombre (self,otro):
        if isinstance (otro,Alumno):
            if self.nombre == otro.nombre:
                return 0

            elif self.nombre < otro.nombre:
                return -1
                
        else:
            return 1

    def cmp_notas(self,otro):
        if isinstance (otro,Alumno):
            if self.nota_media == otro.nota_media:
                return 0
            elif self.nota_media < otro.nota_media:
                return -1
        else:
            return 1
    def imprime_nota(self):
        print( "El alumno: " + self.nombre + " apellido: " + self.apellido + " con la notas: " + str(self.lista) + " tiene una calificación media de: " + str(self.media))
    
    


Al1= Alumno("David", "Díaz")
Al1.pon_nota(5)
Al1.nota_media()
Al1.imprime_nota()


Al2 = Alumno("Maria", "Gómez")
Al2.pon_nota(8)
Al2.pon_nota(4)
Al2.pon_nota(3)
Al2.nota_media()
Al2.imprime_nota()

print(Al1.cmp_nombre(Al2))

class Varios():
    lista_alumnos = []
    def __init__(self, nombre, apellido, evaluacion):
        self.nombre = nombre
        self.apellido = apellido
        self.evaluacion= evaluacion

    def alumnos(self):
        self.alumnos = alumnos
        self.lista_alumnos.append(self.alumnos)
        print(self.lista_alumnos)
    
    def imprime(self):
        print(self.lista_alumnos)
    
    def orden(self):
        self.lista_alumnos().sort
        print(self.lista_alumnos)

    def __str__(self):
        return "Lista de alumnos: " + str(self.lista_alumnos)


Al3 = Varios("Romero", "Gomez", 8)
Al4 = Varios ("Vanesa", "Urqui", 9)
print(Al3)
print(Al4)




