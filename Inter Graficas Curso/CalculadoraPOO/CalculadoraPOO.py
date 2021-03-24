from tkinter import * 
raiz = Tk()

class Calculadora:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora POO")
        #--------------------------------------------------------------------------------------------------------------------------------------
        #-------------------<<<<< Creamos Display >>>>> ---------------------------------------------------------------------------------
        self.display = Entry(ventana, font = "Arial 15")

        #--------------------------------------------------------------------------------------------------------------------------------------
        #-------------------<<<<< Ubicación del  Display >>>>> ---------------------------------------------------------------------------------
        self.display.grid(row=1,column=1,columnspan=4,pady=10)
        self.display.config(background="black", fg="#00db00", justify="right", width=15)
        #--------------------------------------------------------------------------------------------------------------------------------------
        #-------------------<<<<< Creación de botones >>>>> ---------------------------------------------------------------------------------
        boton7 = self.colocar_Boton(7)
        boton8 = self.colocar_Boton(8)
        boton9 = self.colocar_Boton(9)
        botondiv= self.colocar_Boton("/", mostrar = False)
        #-------------------<<<<< Segunda fila >>>>> ---------------------------------------------------------------------------------
        boton4 = self.colocar_Boton(4)
        boton5 = self.colocar_Boton(5)
        boton6 = self.colocar_Boton(6)
        botonmul= self.colocar_Boton("X", mostrar = False)
        #-------------------<<<<< Tercera fila >>>>> ---------------------------------------------------------------------------------
        boton1 = self.colocar_Boton(1)
        boton2 = self.colocar_Boton(2)
        boton3 = self.colocar_Boton(3)
        botonres= self.colocar_Boton("-", mostrar = False)
        #-------------------<<<<< Tercera fila >>>>> ---------------------------------------------------------------------------------
        botoncero = self.colocar_Boton(0)
        botoncoma = self.colocar_Boton(".")
        botoigual = self.colocar_Boton("=", mostrar = False)
        botonresmas= self.colocar_Boton("+", mostrar = False)

        botones =[boton7, boton8, boton9, botondiv,boton4,boton5,boton6,
        botonmul,boton1,boton2,boton3,botonres,botoncero,botoncoma,botoigual,botonresmas]
        contador = 0

        for fila in range(2,6):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1

    def colocar_Boton(self, valor, mostrar=True, ancho = 9, alto= 1 ):
        return Button(self.ventana, text= valor, width=ancho, height=alto)










mi_calculadora = Calculadora(raiz)
raiz.mainloop()