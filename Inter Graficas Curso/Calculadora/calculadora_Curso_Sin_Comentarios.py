from tkinter import*
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()
digitoDisplay= StringVar()

operacion=""

resultado =0
coma = False 
display = Entry(miFrame, textvariable=digitoDisplay, font="Arial 18")
display.grid(row=1, columnspan=5, pady=10)
display.config(background="black", fg="#00db00",justify="right", width=32, font=("Arial",18))

# ---------------------------- Aparicion del CERO autmomaticamente al iniciar la calculadora -------------------------------------------------
digitoDisplay.set("0")
#
# ---------------------------- Pulsaciones numeros -------------------------------------------------

def pulsacionesTeclas(numPulsado):
    global operacion 
    global coma 
    if operacion != "":
        
        digitoDisplay.set(numPulsado)
        operacion = " "
    else:
        if numPulsado == "0" and digitoDisplay.get() == "0":
            digitoDisplay.set("0")
            
        elif numPulsado == "." and digitoDisplay.get() == "0":
            digitoDisplay.set(digitoDisplay.get() + numPulsado)
        
        
        elif numPulsado != "0" and digitoDisplay.get() == "0":
            digitoDisplay.set(numPulsado)
            
        

        else:
            if numPulsado == "." and coma == False:
                digitoDisplay.set(digitoDisplay.get() + numPulsado)
                coma = True
            else:
                if numPulsado == "." and coma == False:
                    digitoDisplay.set(digitoDisplay.get() + numPulsado)
                    coma = True
                elif numPulsado != "." and coma == True:
                    digitoDisplay.set(digitoDisplay.get() + numPulsado)


# ---------------------------- Función suma --------------------------------------------------------
def suma(num):
    
    global operacion
    global resultado
    resultado+=int(num)
    digitoDisplay.set(resultado)
    operacion = "suma"
    
# ---------------------------- Función igual --------------------------------------------------------
def total():
    global resultado
    digitoDisplay.set(resultado + int(digitoDisplay.get()))
    """En la siguiente sentencia le está diciendo que introduzca al Entry lo
    acumulado en el resultado más el valor entero de lo que hay en ese momento en el digitoDisplay
    """
    resultado=0
    """ Luego reseteamos a cero para que no quede las cifras a compañando el resultado final"""

#----------------------------- Primera fila  -------------------------------------------------------

boton7= Button(miFrame, text="7", width=6, command= lambda: pulsacionesTeclas("7"))
boton7.grid( row=2, column=1)

boton8= Button(miFrame, text="8", width=6, command= lambda: pulsacionesTeclas("8"))
boton8.grid( row=2, column=2)

boton9= Button(miFrame, text="9", width=6, command= lambda: pulsacionesTeclas("9"))
boton9.grid( row=2, column=3)

botonD= Button(miFrame, text="/", width=6, )
botonD.grid( row=2, column=4)

#----------------------------- Segunda fila  -------------------------------------------------------

boton4= Button(miFrame, text="4", width=6, command= lambda: pulsacionesTeclas("4"))
boton4.grid( row=3, column=1)

boton5= Button(miFrame, text="5", width=6, command= lambda: pulsacionesTeclas("5"))
boton5.grid( row=3, column=2)

boton6= Button(miFrame, text="6", width=6, command= lambda: pulsacionesTeclas("6"))
boton6.grid( row=3, column=3)

botonM= Button(miFrame, text="*", width=6)
botonM.grid( row=3, column=4)

#----------------------------- Tercera fila  -------------------------------

boton1= Button(miFrame, text="1", width=6, command= lambda: pulsacionesTeclas("1"))
boton1.grid( row=4, column=1)

boton2= Button(miFrame, text="2", width=6, command= lambda: pulsacionesTeclas("2"))
boton2.grid( row=4, column=2)

boton3= Button(miFrame, text="3", width=6, command= lambda: pulsacionesTeclas("3"))
boton3.grid( row=4, column=3)

botonRes= Button(miFrame, text="-", width=6)
botonRes.grid( row=4, column=4)



#----------------------------- Cuarta fila  -------------------------------

boton0= Button(miFrame, text="0", width=6, command= lambda: pulsacionesTeclas("0"))
boton0.grid( row=5, column=1)

botonComa= Button(miFrame, text=".", width=6, command= lambda: pulsacionesTeclas("."))
botonComa.grid( row=5, column=2)

botonIgual= Button(miFrame, text="=", width=6, command= lambda: total())
botonIgual.grid( row=5, column=3)

botonMas= Button(miFrame, text="+", width=6, command=lambda:suma(digitoDisplay.get()))
botonMas.grid( row=5, column=4)














raiz.mainloop()