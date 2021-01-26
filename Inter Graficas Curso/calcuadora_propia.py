from tkinter import *
root =Tk()
root.title("Calculadora Propia")
root.iconbitmap("calculadora.ico")
myFrame = Frame(root, width= "500", height="750", background="#C7B22E" )
myFrame.pack()

caja= Label(myFrame,text=" Te quiero mucho cosita ",width=50, height=3)
caja.place(x=70., y=50)

borrar= Label(myFrame,text="AC",width=10)
borrar.place(x=70,y=105)

convertir= Label(myFrame,text="+/-",width=10)
convertir.place(x=160,y=105)

por= Label(myFrame,text="+/-",width=10)
por.place(x=255,y=105)

cua=Label(myFrame,text="√",width=10)
cua.place(x=350,y=105)


siete= Label(myFrame,text="7",width=10)
siete.place(x=70,y=138)

ocho= Label(myFrame,text="8",width=10)
ocho.place(x=160,y=138)

nueve= Label(myFrame,text="9",width=10)
nueve.place(x=255,y=138)

dividir=Label(myFrame,text="/",width=10)
dividir.place(x=350,y=138)






root.mainloop()