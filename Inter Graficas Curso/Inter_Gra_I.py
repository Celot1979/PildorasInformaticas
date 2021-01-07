from tkinter import *
import tkinter
raiz = Tk()
#Comeinza la app con la raiz
raiz.title("Primera ventana Tkinter")
#raiz.resizable(0,0) #Con este método no podemos redimensionar
#Tanto es así, que no tan si quiera sale el simbolo de poder hacerlo.
#Si en cualquier momento cambiamos el false por un True( que simplememte,
# sería poniendo un 1 en claqueira de los parámetros, cambiaría)
#raiz.resizable(1,0) #En teoria, sólo redimensiona en horizontal

#raiz.iconbitmap("favicon.ico")# Semtencia para crear un icono personalizado

#raiz.geometry("700x400")
raiz.config(bg="pink") # color a la ventana(raiz)
"""" Aquí comenzaré el segundo víeo """
#Vamos a crear el FRAME
miFrame=Frame()

#Para que el nuevo Frame se inegre en la raíz, debemos EMPAQUEARLO.El hecho de empaquetarlo no debe de llevar
#ningún parámetro dentro de los paréntesis. Después de seguir el video nos muestra como alinearlo y otros métodos
#que está en la documentación.
#miFrame.pack(side="bottom")#El frame quedará abajo alineado
#miFrame.pack(side="right")#El frame quedará a la derecha alineado
#miFrame.pack(side="left")#El frame quedará izq alineado
#miFrame.pack(side="top")#El frame quedará abajo alineado

"""Metodo anchor"""
#miFrame.pack(anchor=W)


"""Metodo expand y fill. Deberiamos tener un elemento más como es el widget, pero debemos imginar
al expand como un booleano que afirma o no que se queire expandir el widget y el fill hacia donde
x= Ejercaresiano
y = Eje cartesiano
both= ambos sentidos
none= no se expanda
"""
#miFrame.pack(fill="x")
#miFrame.pack(expand=True, fill="y")
miFrame.pack(expand=True,fill="both")
#miFrame.pack(fill="none")
""" Por automación los frames no tienen ni color ni tamaño, vienen por defecto.
    Para camiar esto seguiremos los siguientes pasos"""


"""Método de ipadx y ipady """
#miFrame.pack(ipadx=10, ipady= 10)
"""Metodo padx y pady """
#miFrame.pack(padx=10,pady=10)


miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(cursor="hand")
#miFrame.config(bitmap="gray25")












raiz.mainloop()
#Al final simepre de toas las app