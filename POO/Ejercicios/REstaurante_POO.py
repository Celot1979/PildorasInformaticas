class Restaurante():
    def __init__(self, docenas, kg):
        self.docenas=docenas
        self.kg = kg
        self.huevos=12
        self.gramos = self.kg * 1000

    def setContar_Huevos_Docenas(self):
        
        self.huevos = self.docenas * self.huevos

    def getContar_Huevos_Docenas(self):
        return "Tenemos: " + str(self.docenas) +" docenas de huevos. Que en número de huevos son: " + str(self.huevos)
    
    def getContar_Gramos_chorizo(self):
        return "Tenemos: " + str(self.kg) +" KG de chorizo. Que en gramos son: " + str(self.gramos) + " grs"
    
    def setPlatos(self,num_pl):
        self.huevos = self.huevos - (num_pl * 2)
        self.gramos = self.gramos - (num_pl *200)
        self.kg = self.gramos/1000
        
        
    def getPlatos(self):
        print("Lo que queda es: " + str(self.huevos) +" huevos" +  " .En kilos de chorizo son " + str(self.kg) + " kg")


d = int(input("¿ Cuantas docenas de huevos hay: ?"))
c = int(input("¿ Cuantas kilos de chorizo: ?"))

res = Restaurante(d,c)
p = int(input("Cuantos platos"))
res.setPlatos(p)
res.getPlatos()

