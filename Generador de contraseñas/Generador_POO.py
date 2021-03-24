from tkinter import * 
from random import randrange, choice
import time
raiz = Tk()

class Generador():
    def __init__(self,ventana):
        self.ventana =ventana
        self.ventana.title("Generador de contraseñas en POO")
        self.ventana.geometry("280x300")
        self.texto = Label(ventana, text="Número de caracteres para la contraseña: ")
        self.texto.grid(row=1,column=5)
        self.entrada_datos = StringVar()
        self.display = Entry(ventana,textvariable= self.entrada_datos)
        self.display.grid(row=3,column=5)
        

        self.display2 = Entry(ventana, text="Número de caracteres para la contraseña: ")
        self.display2.grid(row=7,column=5)
        

        def mostrar(self):
            self.valor = self.display.get()
            print(self.valor)
            for i in range(int(self.valor)):
                self.display2.insert(0, choice(["Z","X","C","V","B","N","M","A","S","D","F","G",
                "H","J","K","L","Ñ","Q","W","E","R","T","Y","U","I","O","P","z","x","c","v","b","n","m","a","s","d","f","g",
                "h","j","k","l","ñ","q","w","e","r","t","y","u","i","o","p","1","2","3",
                "4","5","6","7","8","9","0","?","¿","!","$","&","Ç","*","+"]))
            if int(self.valor) >= 8:
                self.resultado = Label(raiz,text="Contraseña segura")
                self.resultado.grid(row=9,column=5)
                self.resultado.config(fg="Green",font=("Verdana",15))
        
            elif int(self.valor) < 8:
                self.resultado2 = Label(raiz,text="Contraseña No segura", font="red")
                self.resultado2.grid(row=9,column=5)
                self.resultado2.config(fg="Red",font=("Verdana",15))
            
            

        def borrar(self):
            self.display.delete(0,END)
            self.display2.delete(0,END)

        self.Buton1=Button(ventana,text="Generador",command= lambda: mostrar(self))
        self.Buton1.grid(row=5,column=5)
        self.Buton2=Button(ventana,text="Borrar",command=lambda: borrar(self))
        self.Buton2.grid(row=6,column=5)


mi_generador = Generador(raiz)


raiz.mainloop()