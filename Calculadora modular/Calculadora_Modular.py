from tkinter import *

from Botonera_Calculadora import*
raiz = Tk()

class Calculadora:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora POO")
        self.operacion=""
        self.control_punto=0
        #--------------------------------------------------------------------------------------------------------------------------------------
        #-------------------<<<<< Creamos Display >>>>> ---------------------------------------------------------------------------------
        self.display = Entry(ventana, font = "Arial 15")

        #--------------------------------------------------------------------------------------------------------------------------------------
        #-------------------<<<<< Ubicación del  Display >>>>> ---------------------------------------------------------------------------------
        self.display.grid(row=1,column=1,columnspan=4,pady=10)
        self.display.config(background="black", fg="#00db00", justify="right", width=15)
        #--------------------------------------------------------------------------------------------------------------------------------------
        #-------------------<<<<< Creación de botones >>>>> ---------------------------------------------------------------------------------
        boton7 = colocar_Boton(self,7)
        boton8 = colocar_Boton(self,8)
        boton9 = colocar_Boton(self,9)
        botondiv= colocar_Boton(self,"/")
        #-------------------<<<<< Segunda fila >>>>> ---------------------------------------------------------------------------------
        boton4 = colocar_Boton(self,4)
        boton5 = colocar_Boton(self,5)
        boton6 = colocar_Boton(self,6)
        botonmul= colocar_Boton(self,u"\u00D7")
        #-------------------<<<<< Tercera fila >>>>> ---------------------------------------------------------------------------------
        boton1 = colocar_Boton(self,1)
        boton2 = colocar_Boton(self,2)
        boton3 = colocar_Boton(self,3)
        botonres= colocar_Boton(self,"-")
        #-------------------<<<<< Tercera fila >>>>> ---------------------------------------------------------------------------------
        botoncero = colocar_Boton(self,0)
        botoncoma = colocar_Boton(self,".")
        botoigual = colocar_Boton(self,"=", mostrar= False)
        botonresmas= colocar_Boton(self,"+")

        botones =[boton7, boton8, boton9, botondiv,boton4,boton5,boton6,
        botonmul,boton1,boton2,boton3,botonres,botoncero,botoncoma,botoigual,botonresmas]
        construir_botones(self, botones, 4)

mi_calculadora = Calculadora(raiz)

raiz.mainloop()