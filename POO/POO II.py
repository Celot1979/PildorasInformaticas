class Coche():
    ruedas=4 #Propiedades
    largoChasis=260
    anchoChasis=130
    arrancado=False #Creamos una varibale booleana para luego poder usar el método
    
    def arrancar(self):#Método
        self.arrancado=True
    def estadoCoche(self):
        if (self.arrancado): #Si se pone entre parentesis, y dos punto= a una comparación
            return "El coche está funcionando"
        else:
            return "El coche está parado"

              

popo=Coche()#Ejemplar de coche
mazda=Coche()
#print("Tu coche tiene " + str(popo.ruedas) + " ruedas" + " con un largo de chasis: " + str(popo.largoChasis) + " cm "\
    #+ " con un ancho de: " + str(popo.anchoChasis) + " cm ")
popo.arrancar() #Al usar el me´tod, al imprimir, daría TRUE.
#En cambio, si no llamamos al método antes de imprimir, nos imprimiría FALSE
#print("Tu coche está arrancado " + str(popo.arrancado))
print(popo.estadoCoche())
print(mazda.estadoCoche())