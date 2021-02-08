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