from tkinter import *
from tkinter import messagebox as mb
import tkinter
import  csv



root = Tk()
root.title("PROTECTORA")
root.geometry("700x350")
root.config(background="thistle2")

#Imagen de fondo

#imagen = PhotoImage(file="/Users/danielgil/Desktop/Curso_Python/Proctetora2.png")
#Imagen_2 =Label(root, image=imagen)
#Imagen_2.place(x=180, y=220)



#Variables
id= StringVar()
nombre= StringVar()
nombre_animal = StringVar()
chip_animal= StringVar()
lugar_animal= StringVar()
tipo_animal= StringVar()
raza_animal= StringVar()
fecha_animal= StringVar()
ano_animal= StringVar()

#Diccionario y lista
#entrada = []
#dicci={}
#################################################    SEGUNDA VENTANA   ############################################################################################################################################################
#################################################                         ###########################################################################################################################

def Segunda_Ventana():
    root.iconify()
    ventana2=Toplevel()
    ventana2.title("Menu")
    ventana2.geometry("700x350")
    ventana2.config(background="thistle2")
    #label_menu= Label(ventana2, text="MENU", background="thistle2", font=("Arial",30))
    #label_menu.place(x=300, y=0)
    menubar = Menu(ventana2)
    root.config(menu=menubar)
    ######################################## AQUI DECLARAMOS EL MENÚ ########################################################## 
    Animales = Menu(menubar,tearoff=0)
    Adoptantes = Menu(menubar,tearoff=0)
    Visitas = Menu(menubar,tearoff=0)
    Contacto = Menu(menubar,tearoff=0)
    # TEAROF en teoría es porque alguna vez sale un simbolo por defecto. Si bien en Mac no lo veo
    #Es probable que en W10, si salga.

    ######################################### AÑADIMOS LAS PARTES DEL MENÚ ############################################### 
    menubar.add_cascade(label="Animales", menu=Animales )
    menubar.add_cascade(label="Adoptantes", menu=Adoptantes)
    menubar.add_cascade(label="Visitas", menu=Visitas)
    menubar.add_cascade(label="Contacto ", menu=Contacto )

    ################################################## AÑADIMOS SUBMENUS ########################################################## 
    #Nueva ventana emergente al presionar NUEVA ALTA, con su función correspondient
    #################################################    TERCERA VENTANA   ############################################################################################################################################################
    #################################################                         ###########################################################################################################################

    def nueva_adopcion():
        ventana2.destroy()
        #Ventana nueva donde se hará rellenará los datos del animal adoptado
        entrada = Toplevel()
        entrada.title("Bienveni@ a nuestra casa")
        entrada.geometry("700x350")
        entrada.config(background="thistle2")
        # Label de la página con sus configuraciones
        id= Label(entrada, text ="ID")
        id.place(x=100, y=0)
        id.config(bg="thistle2")


        nombre= Label(entrada, text ="Nombre")
        nombre.place(x=100, y=30)
        nombre.config(bg="thistle2")

        chip= Label(entrada, text="Chip")
        chip.place(x=100, y= 60 )
        chip.config(bg="thistle2")

        lugar= Label(entrada, text="Lugar")
        lugar.place(x=100, y= 90 )
        lugar.config(bg="thistle2")

        tipo= Label(entrada, text="Tipo")
        tipo.place(x=100, y= 120 )
        tipo.config(bg="thistle2")

        tipo_raza= Label(entrada, text="Raza")
        tipo_raza.place(x=100, y= 150 )
        tipo_raza.config(bg="thistle2")

        fecha_entrada=Label(entrada, text="Fecha de admisión")
        fecha_entrada.place(x=100, y= 180)
        fecha_entrada.config(bg="thistle2")

        ano=Label(entrada, text="Años ")
        ano.place(x=100, y=210)
        ano.config(bg="thistle2")

        # Entry de la página con sus configuraciones
        i = 0
        def click_boton(valor):
            global i
            id_txt.insert(i, valor) 
            i+=1
        id_txt= Entry(entrada, width=20, textvariable=id)
        id_txt.place(x=200, y=0)
        

        nombre_txt= Entry(entrada, width=20, textvariable=nombre_animal)
        nombre_txt.place(x=200, y=30)
        
        chip_txt= Entry(entrada, width=20, textvariable=chip_animal)
        chip_txt.place(x=200, y=60)

        lugar_txt= Entry(entrada, width=20, textvariable=lugar_animal)
        lugar_txt.place(x=200, y=90)

        tipo_txt= Entry(entrada, width=20, textvariable=tipo_animal)
        tipo_txt.place(x=200, y=120)

        tipo_raza_txt= Entry(entrada, width=20, textvariable=raza_animal)
        tipo_raza_txt.place(x=200, y=150)
        
        fecha_txt= Entry(entrada, width=20, textvariable=fecha_animal)
        fecha_txt.place(x=200, y=180)

        ano_txt= Entry(entrada, width=20, textvariable=ano_animal)
        ano_txt.place(x=200, y=210)

        # Botones y funciones
        #entrada=[]
        def borrar_datos_registro():
            id_txt.delete(0,END)
        

            nombre_txt.delete(0,END)
        
            chip_txt.delete(0,END)
 
            lugar_txt.delete(0,END)

            tipo_txt.delete(0,END)

            tipo_raza_txt.delete(0,END)
        
            fecha_txt.delete(0,END)

            ano_txt.delete(0,END)

        def grabar():
            di={"ID: ": id_txt.get(), "Nombre: " : nombre_txt.get(), "Chip: ": chip_txt.get() , "Lugar: ": lugar_txt.get(),"Familia: ": tipo_txt.get(), "Raza: ": tipo_raza_txt.get(), "Fecha: ": fecha_txt.get(), "Años: ": ano_txt.get()   }
            with open("Registro.csv", "w") as csv_file:
                write = csv.writer(csv_file)
                for key, value in di.items():
                    write.writerow([key, value])
            mb.showinfo("Registro realizado con éxito", id_txt.get() + " " + " "+ nombre_txt.get() + " " + chip_txt.get() + " " + lugar_txt.get() + " " + tipo_txt.get() + " "+ tipo_raza_txt.get()+ " "+ " " +  fecha_txt.get() + " " + ano_txt.get())
            #print(di)
            borrar_datos_registro()

        boton_nombre_animal = Button(entrada, text="GRABAR", command=grabar, activebackground="#F50743")
        boton_nombre_animal.place(x=200, y=250)
        
    Animales.add_command(label="Nueva alta", command= nueva_adopcion)
    Animales.add_command(label="Editar datos")
    Animales.add_command(label="Baja del sistema por adopción")
    
    ######################################### SEPARDOR Y SALIR ########################################################## 
    Animales.add_separator()
    def off():
        ventana2.destroy()
        root.destroy()
    Animales.add_command(label="Salir", command=off)

    ventana2.mainloop()
    #OJO!!! todo lo que se tenga que crear en la nueva ventana tiene que estar en está función
    





#################################################    PANTALLA PRINCIPAL   ############################################################################################################################################################
#################################################                         ###########################################################################################################################
label_cuenta= Label(root, text="CUENTA USUARIO", background="thistle2", font=("Arial",30))
label_cuenta.place(x=180, y=0)

label_nombre= Label(root, text="Nombre",background="thistle2", font=("Arial",12))
label_nombre.place(x=100, y=80)

label_password = Label(root, text="Contraseña",background="thistle2", font=("Arial",12))
label_password.place(x=100, y=120)

entry_nombre= Entry(root, width=20, textvariable=nombre)
entry_nombre.place(x=200, y=86)

entry_password= Entry(root, width=20)
entry_password.place(x=200, y=120)
entry_password.config(show="*")
######################################## VALIDAR LOS CAMPOS EN PAGINA PRINCIPAL ########################################################## 
def validar():
    if entry_nombre.get() == "Dani":
        if entry_password.get() == entry_password.get():
            #mb.showinfo("Correcto", entry_nombre.get() + " \nContraseña: " + entry_password.get())
            Segunda_Ventana()
    else:
        mb.showerror("No es la contraseña correcta")

boton_nombre= Button(root, text="VALIDAR", command=validar)
boton_nombre.place(x=150, y=180)
#boton_nombre.config(background="thistle2")
######################################## BORRAR CAMPOS DE LA PÁGINA PRINCPIAL ########################################################## 
def borrar():
    entry_nombre.delete(0, END)
    entry_password.delete(0, END)
boton_nombre_borrar= Button(root, text="BORRAR", command=borrar, activebackground="#F50743")
boton_nombre_borrar.place(x=250, y=180)
#boton_nombre.config(background="thistle2")


######################################## SALIR DE LA PÁGINA PRINCIPAL ########################################################## 

def salir_principal():
        root.destroy()
        """Función para que al presionar el boton salir en la página principal se cierre el programa"""
        
boton_salir= Button(root, text="SALIR", command=salir_principal, activebackground="#F50743")
boton_salir.place(x=350, y=180)






root.mainloop()