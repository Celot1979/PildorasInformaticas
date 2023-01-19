import socket
from tkinter import *


root = Tk()
root.geometry("5000x5000")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
root.title("Localizador de nombres de equipos - IPs")
Nombre_equipo= Label(text ="Nombre del equipo",background="azure",font=("Monaco",18))
Nombre_equipo.place(x=800, y=80)
Ip_Label= Label(text ="IP",background="azure",font=("Monaco",18))
Ip_Label.place(x=800, y=160)

Pantalla_nombre= Label(text =hostname,background="azure",font=("Monaco",18))
Pantalla_nombre.place(x=1000, y=80)
Pantalla_IP= Label(text =ip,background="azure",font=("Monaco",18))
Pantalla_IP.place(x=1000, y=160)


#print("El nombre del ordenador es : " + hostname + "\n" + "La dirección IP es. " + ip)

root.mainloop()