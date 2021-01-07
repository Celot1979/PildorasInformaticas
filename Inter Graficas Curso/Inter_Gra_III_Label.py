from tkinter import * 
root = Tk()
root.title("Label")
miFrame=Frame(root, width="750", height="350",bg="silver")
miFrame.pack()
"""En caso que la variable vaya a cambiar a lo largo
del program, tenga acciones, etc. Se deberá crear una 
variable como se ve en el ejemplo.
Por supuesto se deberá empaquetar. Si se empaqueta con
.pack(),la ventana tendrá por defecto la medida de la 
etiqueta( muy pequeña). Si deseamos cambiar eso, debemos
empauetarla en una .place() """
#miLabel= Label(miFrame,text="7 de Enero 2021")
#miLabel.place(x = 120, y = 125)

""" Si como es el caso del ejemplo que nos proponemos
ahora es muy simple el Label y sabemos que no sufrirá cambios
podemos abreviar muchísimo el código """
#Label(miFrame,text="sintasis abreviada",fg="blue",font=("Courier",30)).place(x=120,y=200)

""" Label no sólo trabaja con texto, también puede trabajar con
imágenes """
miLogo = PhotoImage(file= "mano.png")
Label(miFrame, image=miLogo).place(x=120,y=125)#Imprescindible colocar las x e y


root.mainloop()