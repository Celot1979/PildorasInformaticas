from tkinter import*
from random import randrange, choice
import time



        

    


raiz = Tk()
raiz.title("Generador de contraseñas")
raiz.geometry("280x300")
Texto1 = Label(raiz, text="Número de caracteres para la contraseña: ")
Texto1.grid(row=1,column=5)
Texto1.config(anchor=CENTER)
entrada_datos= StringVar()
datos= StringVar()

display = Entry(raiz,textvariable= entrada_datos)
display.grid(row=3,column=5)
display2 = Entry(raiz, textvariable= datos)
display2.grid(row=7,column=5)






    
    

def mostrar():
    valor= display.get()
    for i in range(int(valor)):
        display2.insert(0, choice(["Z","X","C","V","B","N","M","A","S","D","F","G",
    "H","J","K","L","Ñ","Q","W","E","R","T","Y","U","I","O","P","z","x","c","v","b","n","m","a","s","d","f","g",
    "h","j","k","l","ñ","q","w","e","r","t","y","u","i","o","p","1","2","3",
    "4","5","6","7","8","9","0","?","¿","!","$","&","Ç","*","+"]))

    
    if int(valor) >= 8:
        resultado = Label(raiz,text="Contraseña segura")
        resultado.grid(row=9,column=5)
        resultado.config(fg="Green",font=("Verdana",15))
        
    elif int(valor) < 8:
        resultado2 = Label(raiz,text="Contraseña No segura", font="red")
        resultado2.grid(row=9,column=5)
        resultado2.config(fg="Red",font=("Verdana",15))
        

    
        
 

boton1= Button(raiz,text="Generador",command= mostrar)
boton1.grid(row=5,column=5)



def borrar():
    display.delete(0,END)
    display2.delete(0,END)
    
    

boton2= Button(raiz,text="Borrar",command=borrar)
boton2.grid(row=6,column=5)






raiz.mainloop()






