from tkinter import *
raiz= Tk()
raiz.title("Ventana de pruebas")
raiz.iconbitmap("t.ico")
raiz.config(bg="brown")

miFrame= Frame()# Comenzamos el Frame
miFrame.pack()# Esté es el segundo paso, hay que empaquetarlo
#Decirle a al raiz que existe
# Si deseamos que se alinee en la raíz se puede usar, dentro de los parentesis
#(side="right" o side="left" 0 side= center p side = bottom - quedaría en la parte inferior)
#Si queremos que por ejemplo sea arria ala izq hay que usar el parámetro anchor
# sería de la sigueinte forma:
# side= "left", anchor= "n"( archor usa los puntos cardinales n,s,nw,sw)
miFrame.config(bg="red") #Darl color a Frame

miFrame.config(width= "650", height="350") #Es importante darle un tamaño
#si no no tendrá apariencia al darle play

raiz.mainloop()

#Se deja en el vídeo 43 min 09:45