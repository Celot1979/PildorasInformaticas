from tkinter import*
from tkinter import messagebox as mb
import csv
from functools import partial
root = Tk()
root.title("PROTECTORA")
root.geometry("700x350")
root.config(background="thistle2")
########################################### VENTANA PRINCIPAL #################################################################################################################################
############################################################################################################################################################################
#Variables
nombre=StringVar()
password= StringVar()

titulo_ventana= Label(root, text="Cuenta Usuario", font=("Arial",20))
titulo_ventana.place(x=250, y= 0)
titulo_ventana.config(background="thistle2")

Label_Nombre= Label(root, text="NOMBRE", font=("Arial",12))
Label_Nombre.place(x=240, y= 80)
Label_Nombre.config(background="thistle2")

Entry_Nombre= Entry(root, width=20, textvariable=nombre)
Entry_Nombre.place(x=360, y=84)

Label_Password= Label(root, text="CONTRASEÑA", font=("Arial",12))
Label_Password.place(x=240, y= 120)
Label_Password.config(background="thistle2")

Entry_Password= Entry(root, width=20, textvariable=password)
Entry_Password.place(x=360, y=124)
Entry_Password.config(show="*")
########################################### BOTONES Y FUNCIONES VENTANA PRINCIPAL #################################################################################################################################
########################################### BOTON VALIDAR VENTANA PRINCIPAL #################################################################################################################################

def validar():
    if Entry_Nombre.get() == "Dani":
        if Entry_Password.get() == Entry_Password.get():
            #mb.showinfo("correcto", Entry_Nombre.get())
            Segunda_ventana()
        else:
            mb.showwarning("Incorrecto", Entry_Password.get())
    else:
        mb.showerror("Error", Entry_Nombre.get())

boton_validar= Button(root, text="CONECTAR", command=validar)
boton_validar.place(x=240, y=180)

########################################### BOTON BORRAR VENTANA PRINCIPAL #################################################################################################################################
def borrar():
    Entry_Nombre.delete(0,END)
    Entry_Password.delete(0,END)

boton_borrar= Button(root, text="BORRAR", command=borrar)
boton_borrar.place(x=340, y=180)

########################################### BOTON SALIR VENTANA PRINCIPAL #################################################################################################################################

def salir():
    root.destroy()
boton_salir= Button(root, text="SALIR", command=salir)
boton_salir.place(x=440, y=180)

########################################### SEGUNDA VENTANA PRINCIPAL #################################################################################################################################
############################################################################################################################################################################

def Segunda_ventana():
    root.iconify()
    ventana2 = Toplevel()
    ventana2.title("Menu")
    ventana2.geometry("700x350")
    ventana2.config(background="thistle2")
    menubar= Menu(ventana2)
    menuArchivo= Menu(menubar)
    
    ######################Aqui declaramos el menú ###################################################
    Animales= Menu(menubar, tearoff=0)
    Adoptantes = Menu(menubar,tearoff=0)
    Visitas = Menu(menubar,tearoff=0)
    Contacto= Menu(menubar,tearoff=0)

    ###################### Crear los comandos del  menú  ###################################################
    menubar.add_command(label="Animales",Menu= Animales)
    menubar.add_command(label="Adoptantes", menu= Adoptantes)
    menubar.add_command(label="Visitas", menu = Visitas)
    menubar.add_command(label="Contacto", menu= Contacto)
    
    ###################### Agregar los menús a la barra de Menús  ###################################################
    menubar.add_cascade(label="Animales", menu= menuArchivo, )
    menubar.add_cascade(label="Adoptantes", menu= menuArchivo)
    menubar.add_cascade(label="Visitas", menu= menuArchivo)
    menubar.add_cascade(label="Contacto", menu= menuArchivo)

    ###################### Añadimos  SubMenús  ###################################################
    Animales.add_command(label="Nueva alta", menu= Animales)
    




    

    ventana2.config(menu=menubar)
    



    ventana2.mainloop()



root.mainloop()