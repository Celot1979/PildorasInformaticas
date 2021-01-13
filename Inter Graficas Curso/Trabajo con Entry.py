from tkinter import*
raiz = Tk()
miFrame= Frame(raiz, width=1000, height=550)
miFrame.pack()

#-----------------------------------------------
nombreLabel= Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky=W)
#El método sticky es para la alineción del texto del label
cuadroTexto= Entry(miFrame)
cuadroTexto.grid(row=0, column=1)
#Para hacer cambios en los entrys, debemos usar el método .config. Y luego usar métodos iguales a los de
# Label.ej:
cuadroTexto.config(fg="red")
#Si le damos a iniciar el programa nos daremos cuenta que donde el usuario escribirá, las letras se mostrarán en rojo.
#Mientras, en los demás Entrys, seguirá siendo en negro
#-----------------------------------------------
nombreLabel2= Label(miFrame, text="Apellidos: ")
nombreLabel2.grid(row=1, column=0, sticky=W)
cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=1, column=1)
#-----------------------------------------------
nombreLabel3 = Label(miFrame, text="Dirección: ")
nombreLabel3.grid(row=2, column=0, sticky=W)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=2, column=1)
#-----------------------------------------------
nombreLabel4 = Label(miFrame, text="Email: ")
nombreLabel4.grid(row=3, column=0, sticky=W)
cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=3, column=1)



#-----------------------------------------------




raiz.mainloop()