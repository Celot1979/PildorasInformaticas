from tkinter import *
raiz= Tk()#Ventana
raiz.title("Ventana de pruebas")#Titulo de ventana
#raiz.resizable(1,1)# podemos dar unas medidas predefinidas , 
#con 0,0 no deja redimensionar. Si en el algno de los dos ponemos un 1 nos deja en esa parte redimensionar
""" Para cambiar el icono debe de ser de extensión .ico y con unas dimesiones
se peude convertir en ( conversor.ico)"""

raiz.iconbitmap("t.ico")#Para poner un icono
#raiz.geometry("500 X 500") # Darle una medida a la ventana
raiz.config(bg="brown")
raiz.mainloop()#loop imprescindible