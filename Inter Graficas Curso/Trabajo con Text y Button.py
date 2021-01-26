from tkinter import*
raiz = Tk()
miFrame= Frame(raiz, width=1000, height=550)
miFrame.pack()

#----------------------------------------------- LABEL Y ENTRY DE NOMBRE ------------------------------------------------------
nombreLabelNombre= Label(miFrame, text="Nombre: ")
nombreLabelNombre.grid(row=0, column=0, sticky=W)
#El método sticky es para la alineción del texto del label
cuadroTextoNombre= Entry(miFrame)
cuadroTextoNombre.grid(row=0, column=1, padx=15, pady=15)
""" Vamos a introduccir los PADX y PADY, y lo haremos en los
GRID DE LOS ENTRT"""
#Para hacer cambios en los entrys, debemos usar el método .config. Y luego usar métodos iguales a los de
# Label.ej:
cuadroTextoNombre.config(fg="red")
#Si le damos a iniciar el programa nos daremos cuenta que donde el usuario escribirá, las letras se mostrarán en rojo.
#Mientras, en los demás Entrys, seguirá siendo en negro

#---------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------------- LABEL Y ENTRY DE APELLIDOS ------------------------------------------------------
nombreLabelApellidos= Label(miFrame, text="Apellidos: ")
nombreLabelApellidos.grid(row=1, column=0, sticky=W)

cuadroTextoApellidos=Entry(miFrame)
cuadroTextoApellidos.grid(row=1, column=1, padx=15, pady=15)
#---------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------- LABEL Y ENTRY DE CONTRASEÑA ------------------------------------------------------

"""CONTRASEÑA CON ASTERISCOS"""
nombreLabelContraseña= Label(miFrame, text="Contraseña: ")
nombreLabelContraseña.grid(row=2, column=0, sticky=W)

cuadroTextoContraseña=Entry(miFrame)
cuadroTextoContraseña.grid(row=2, column=1, padx=15, pady=15)
cuadroTextoContraseña.config(show="*")
#---------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------- LABEL Y ENTRY DE DIRECCION ------------------------------------------------------

nombreLabeDireccion = Label(miFrame, text="Dirección: ")
nombreLabeDireccion.grid(row=3, column=0, sticky=W)

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=3, column=1, padx=15, pady=15)
#---------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------- LABEL Y ENTRY DE EMAIL ------------------------------------------------------

nombreLabeEmail = Label(miFrame, text="Email: ")
nombreLabeEmail.grid(row=4, column=0, sticky=W)

cuadroTextoEmail=Entry(miFrame)
cuadroTextoEmail.grid(row=4, column=1, padx=15, pady=15)
#---------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------- LABEL Y ENTRY DE CAJA DE TEXTO (para añadir el widget de texto) ------------------------------------------------------

nombreLabeComentarios = Label(miFrame, text="Comentarios: ")
nombreLabeComentarios.grid(row=5, column=0, sticky=W)

cuadroTextoComentarios= Text(miFrame, width= 26, height= 30)
cuadroTextoComentarios.grid(row=5, column=2, padx=15, pady=15)

#Añadir una barra vertical para poder desplazarse en la caja texto
miScrollVertical= Scrollbar(miFrame, command=cuadroTextoComentarios.yview)
miScrollVertical.grid(row=5, column=3, sticky="nsew") # Para que la barra se desplace a lo largo de la caja
cuadroTextoComentarios.config(yscrollcommand= miScrollVertical.set)
#---------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------- BUTTON ------------------------------------------------------

botonEnviar= Button(raiz, text = "Enviar")
botonEnviar.pack()

raiz.mainloop()