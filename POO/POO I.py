class Coche():
    ruedas=4
    largoChasis=260
    anchoChasis=130
    
    def arrancar(self):
        pass

popo=Coche()#Ejemplar de coche
print("Tu coche tiene " + str(popo.ruedas) + " ruedas" + " con un largo de chasis: " + str(popo.largoChasis) + " cm "\
    + " con un ancho de: " + str(popo.anchoChasis) + " cm ")
