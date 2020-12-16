from tkinter import *
raiz = Tk()
#Comeinza la app con la raiz
raiz.title("Primera ventana Tkinter")
#raiz.resizable(0,0) #Con este método no podemos redimensionar
#Tanto es así, que no tan si quiera sale el simbolo de poder hacerlo.
#Si en cualquier momento cambiamos el false por un True( que simplememte,
# sería poniendo un 1 en claqueira de los parámetros, cambiaría)
#raiz.resizable(1,0) #En teoria, sólo redimensiona en horizontal

#raiz.iconbitmap("favicon.ico")# Semtencia para crear un icono personalizado

raiz.geometry("700x400")
raiz.config(bg="pink") # color a la ventana(raiz)











raiz.mainloop()
#Al final simepre de toas las app