from tkinter import *
root = Tk()
root.title("Pruebas con label")
miFrame = Frame()
miFrame.config(width="750", height="350")
miFrame.config(bg="silver")
miFrame.pack()                                                                                                                                                                               
l1 = Label(miFrame,text="Test", fg="black", bg="white")
l2 = Label(miFrame,text="Test", fg="black", bg="white")
l1.pack()
l2.pack()






root.mainloop()