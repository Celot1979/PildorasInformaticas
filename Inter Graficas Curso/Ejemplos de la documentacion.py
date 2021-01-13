import tkinter as tk


def aceptar():
    try:
        n = int(var_texto.get())  # Obtenemos el número de la StringVar
    except ValueError:            # Si lo ingresado no es un entero
        var_lbl.set(f"No escogiste un número válido")
    else:                         # Si lo ingresado es un entero
        var_lbl.set(f"Escogiste el número: {n}")


root = tk.Tk()

var_texto = tk.StringVar()
var_lbl = tk.StringVar()

mi_label = tk.Label(root, textvariable=var_lbl)
var_lbl.set("Escoge un número") # Contenido inicial del Lable
mi_label.grid(row=0, column=0, columnspan=3)

cuadro_texto = tk.Entry(root, textvariable=var_texto)
cuadro_texto.grid(row=1, column=0, columnspan=2)

btn_aceptar = tk.Button(root, text="Aceptar", command=aceptar)
btn_aceptar.grid(row=1, column=2)

root.mainloop()