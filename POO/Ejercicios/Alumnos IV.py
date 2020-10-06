class Alumno():
    def __init__(self,nombre):
        self.nombre=nombre
       
    
    def evaluacion(self,nota):
        self.nota=nota
        if self.nota >= 5:
            print("El alumno " + self.nombre + " ha sacado una nota " + str(self.nota) + " y está aprobado")
            print("Si irá a la Universidad ")
            
        else:
            print("El alumno " + self.nombre + " ha sacado una nota " + str(self.nota) + " y está suspenso")
            print("No irá a la Universidad ")


class Centro(Alumno):
    def __init__(self,nombre,centro):
        Alumno.__init__(self,nombre)
        self.centro = centro
    def __str__(self):
        return "El alumno " + self.nombre + " cursa sus estudios en " + self.centro

    def evaluacion(self):
        
        return super().evaluacion(int(input("¿ qué nota tiene ?: \n ")))


#---------------------------------------------------------
A1 = Alumno("daniel")
A1.evaluacion(9)
#---------------------------------------------------------
A2 = Centro("Lorena", "INS Carreño Miranda")
print(A2)
A2.evaluacion()
#---------------------------------------------------------