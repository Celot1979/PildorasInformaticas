from tkinter import *

def mostrar_pantalla(self,valor):
    self.display.insert(END, valor)

def borrado(self):
    self.display.delete(0, END)