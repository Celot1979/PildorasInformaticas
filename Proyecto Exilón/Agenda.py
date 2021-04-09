#Agenda Python con SQLITE
from tkinter import*
#variables
ANCHO = 560
ALTO = 540
POSX= 400
POSY= 400
anchoAlto= (str(ANCHO) + "x" + str(ALTO))
posicionX = "+" + str(POSX)
posicionY = "+" + str(POSY)
colorVentana = "blue"
colorFondo = "blue"
colorLetra = "white"
#FUNCIONES
def mostrarMensaje():
    print("Prueba")

ventana = Tk()
ventana.config(bg= colorVentana)
ventana.geometry(anchoAlto + posicionX + posicionY)
ventana.title("Agenda")
ID = IntVar()
nombre= StringVar()
apellido = StringVar()
telefono = StringVar()
email = StringVar()

#Etiquetas ,widgets

etiquetaId= Label(ventana, text= "ID.").place(x=50, y=50)
cajaID=Entry(ventana, textvariable=ID).place(x=130, y= 50)
etiquetaNombre= Label(ventana, text="Nombre.").place(x=50, y=90)
cajaNombre = Entry(ventana, textvariable= nombre).place(x=130, y= 90)
etiquetaApellidos= Label(ventana, text="Apellidos.").place(x=50, y=130)
cajaApellidos = Entry(ventana, textvariable= apellido).place(x=130, y= 130)
etiquetaTelefono =Label(ventana, text="Teléfono.").place(x=50, y=170)
cajaTelefono = Entry(ventana, textvariable= telefono).place(x=130, y= 170)
etiquetaEmail =Label(ventana, text="Email.").place(x=50, y=210)
cajaEmail = Entry(ventana, textvariable= email).place(x=130, y= 210)

text = Text(ventana)
text.place(x=50, y=240, width=400, height=200)

#Botones
botonAdd= Button(ventana,text="Añadir", command=mostrarMensaje).place(x=150, y= 500)
botonBorrar= Button(ventana,text="Borrar", command=mostrarMensaje).place(x=200, y= 500)
botonBuscar= Button(ventana,text="Buscar", command=mostrarMensaje).place(x=250, y= 500)
botonModificar= Button(ventana,text="Modificar", command=mostrarMensaje).place(x=300, y= 500)

ventana.mainloop()
