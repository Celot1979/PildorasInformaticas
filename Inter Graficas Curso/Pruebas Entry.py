from tkinter import*
import csv
#---------------------------------------------- funcion-------------------------------------------------------------
entrada = []
dicci={}

def Show():
    print("Nombre: %s\nApellidos: %s\nDireccion: %s\nEmail: %s" % (E1.get(), E2.get(), E3.get(),E4.get()))
    myLabeAceptado= Label(myFrame,text="Mostrado", fg="green")
    myLabeAceptado.grid(row=4,column=1,sticky=W)

    
def Record():
    dicci={"Nombre": E1.get(), "Apellidos": E2.get(), "Dirección": E3.get(), "Email": E4.get()}
    entrada.append(dicci)
    with open("ingreso.csv", "w") as csv_file:
        write = csv.writer(csv_file)
        for key, value in dicci.items():
            write.writerow([key, value])
    print(entrada)
    myLabeAceptado= Label(myFrame,text="Record", fg="green")
    myLabeAceptado.grid(row=4,column=1,sticky=W)
def Delete():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    myLabeAceptado= Label(myFrame,text="Delete", fg="red")
    myLabeAceptado.grid(row=4,column=1,sticky=W)




#-----------------------------------------------------------------------------------------------------------

#---------------------------------------------- Root -------------------------------------------------------------

root = Tk()
root.title("Pruebas")
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------- Frame -------------------------------------------------------------

myFrame = Frame(root, width= "750", height="350", bg="blue")
myFrame.pack()
#---------------------------------------------- Label and Grid -------------------------------------------------------------
var_lbl = StringVar()
myLabel= Label(myFrame,text="Nombre")
myLabel.grid(row=0,column=1,sticky=W)
myLabel2= Label(myFrame,text="Apellidos")
myLabel2.grid(row=1,column=1,sticky=W)
myLabel3= Label(myFrame,text="Direccion")
myLabel3.grid(row=2,column=1,sticky=W)
myLabel4= Label(myFrame,text="Email")
myLabel4.grid(row=3,column=1,sticky=W)

#---------------------------------------------- Entry and Grid -------------------------------------------------------------
nombre = StringVar()
apellidos= StringVar()
direccion = StringVar()
email= StringVar()
var_lbl = StringVar()
E1 = Entry(myFrame,textvariable=nombre, justify=CENTER)
E1.grid(row=0, column=2)

E2 = Entry(myFrame, textvariable=apellidos, justify=CENTER)
E2.grid(row=1, column=2)

E3 = Entry(myFrame, textvariable=direccion, justify=CENTER)
E3.grid(row=2, column=2)

E4 = Entry(myFrame, textvariable=email, justify=CENTER)
E4.grid(row=3, column=2)
#---------------------------------------------- StringVar -------------------------------------------------------------
miSeleccion = StringVar()


#---------------------------------------------- Button -------------------------------------------------------------
Boton1= Button(myFrame, text="Quit", command=myFrame.quit).grid(row=5,column=1,sticky=W,pady=4)
Boton2= Button(myFrame, text="Delete", command=Delete).grid(row=5, column=2,sticky=W,pady=4)
Boton3= Button(myFrame, text="Show", command=Show).grid(row=5,column=3,sticky=W,pady=4)
Boton4= Button(myFrame, text="Record", command=Record).grid(row=5,column=4,sticky=W,pady=4)





root.mainloop()