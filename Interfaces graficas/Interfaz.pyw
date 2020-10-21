from tkinter import *
raiz= Tk()
raiz.title("Ventana de pruebas")
""" Si no queremos que se redimensione"""
#raiz.resizable(0,0)

raiz.iconbitmap("logo.ico")
#raiz.geometry("650x350")
raiz.config(bg="brown")
#---------------------------------------------------------------------------
#1ºVamos a construir un FRAME

miFrame= Frame()
#2ºTenemos que empaquetar el Frame en la raíz
miFrame.pack()

miFrame.config(bg="red")

#3º Hay que dar un tamaño al frame
miFrame.config(width="650", height="350")

#4º colocación del frame ( una sola opcion)
#miFrame.pack(side="right")
#miFrame.pack(side="left")
#miFrame.pack(side="bottom")
#miFrame.pack(side="top")

#5º Colocar un Frame pero con dos opciones de colocación
#miFrame.pack(side="left", anchor= "n") # n = Norte, W= Oeste , s = Sur , e = Este

#6º Existe el rellenado de la raiz con el frame
#miFrame.pack(fill="x") # Pueden ser "x", "y", "both", "none"

#7º Si queremos que también rellene en vertical debemos usar el expand
#miFrame.pack(fill="both", expand="True")#Asi se expandería en toda la raíz

#8ª Para cambiar el borde
miFrame.config(bd=35)# Cantidad de borde
miFrame.config(relief="sunken")#tipo de borde


#9º Cambio de cursor dentro del frame

miFrame.config(cursor="hand2")









raiz.mainloop()