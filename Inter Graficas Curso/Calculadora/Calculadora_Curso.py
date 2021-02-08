from tkinter import*
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()
digitoDisplay= StringVar()

display = Entry(miFrame, textvariable=digitoDisplay, font="Arial 18")
display.grid(row=1, columnspan=5, pady=10)
display.config(background="black", fg="#00db00",justify="right", width=32, font=("Arial",18))
#Display está justamente para darle un color negro de fondo, una letra verde
# y una justificación a la derecha


# ---------------------------- Pulsaciones numeros ------------------------

def pulsacionesTeclas(numPulsado):
    digitoDisplay.set(digitoDisplay.get() + numPulsado)
    """El metodo set sabeos que es para introduccir datos en el entry.
    A continuación usamos el metodo get para que lea que hay en el display del entry,
    y como la función está sólo asociada al 7, si pulsamos otra vez el 7 lo escribirá a 
    continuación del último número escrito. """
#----------------------------- Primera fila  -------------------------------

boton7= Button(miFrame, text="7", width=6, command= lambda: pulsacionesTeclas("7"))
boton7.grid( row=2, column=1)

boton8= Button(miFrame, text="8", width=6, command= lambda: pulsacionesTeclas("8"))
boton8.grid( row=2, column=2)

boton9= Button(miFrame, text="9", width=6, command= lambda: pulsacionesTeclas("9"))
boton9.grid( row=2, column=3)

botonD= Button(miFrame, text="/", width=6, )
botonD.grid( row=2, column=4)

#----------------------------- Segunda fila  -------------------------------

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

botonComa= Button(miFrame, text=",", width=6, command= lambda: pulsacionesTeclas("."))
botonComa.grid( row=5, column=2)

botonIgual= Button(miFrame, text="=", width=6)
botonIgual.grid( row=5, column=3)

botonMas= Button(miFrame, text="+", width=6)
botonMas.grid( row=5, column=4)














raiz.mainloop()