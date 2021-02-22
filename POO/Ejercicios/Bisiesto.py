class Bisiesto():
    def __init__(self, an) :
        
        self.agno = an
       

    def setDatos(self):
        if self.agno % 4 == 0 and self.agno % 100 != 0 or self.agno % 400 == 0 :
            return "Bisiesto"
        else:
            return "NO Bisiesto"



p = int(input("Inroduce el año: "))
prueba = Bisiesto(p)
print(prueba.setDatos())