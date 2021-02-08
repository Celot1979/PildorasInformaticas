from tkinter import *
import parser
#Documents/ Documentado
#By Daniel Gil

#Root
root =Tk()
root.title("Calculadora Propia")#Titulo / Title
root.iconbitmap("calculadora.ico")#Imagen asociada a la aplicacion / Image associated with the application

display = Entry(root,justify= RIGHT,width=22, font="bold", fg="blue")
display.grid(row=1, columnspan=6)
display.config(font=("Arial",30))
#Hacemos más grande el tamaño de la tipografia / We make the font size bigger

#Funciones / Funcions

def clear_display():
    display.delete(0,END)
    #Función de borrado de la entrada / Delete input function
i = 0
def clic_boton(n):
    global i
    display.insert(i, n)
    i += 1
    """Función para que al escribir los número vayan correlativos. 
    El motivo es que si no al escribir uno en el entrada borraría al anterior.
    
    Function so that when writing the numbers they go correlative.
    The reason is that if not writing one in the entry would erase the previous one."""

def calcular():
    display_state= display.get()
    try:
        math_expression =parser.expr(display_state).compile()
        result=eval(math_expression)
        clear_display()
        display.insert(0, result)
    except expression as identifier:
        clear_display()
        display.insert(0, "Error")

    """En está función nos sirve para calcular las operaciones que el usuario vaya realizando en la
    calculadora.
    1º Devolvemos lo que tenemos en la entrada con el método get.
    2º Creamos un try(prueba) en el que vamos evaluando lo siguiente:
       2.1 Mediante la libreria parser (recoge expresiones en formato String, le pasamos como 
       parámetro la entrada.
       2.2 Con el método eval( evalua es expresión que hemos capturado en el método parser))
       2.3 Limpiamos la entrada
       2.4 Insertamos el resultado del método eval.
    3º Creamos una excepción por si la prueba falla. 
    
    In this function it helps us to calculate the operations that the user will perform in the
    calculator.
    1º We return what we have in the input with the get method.
    2º We create a try (test) in which we evaluate the following:
       2.1 Through the parser library (it collects expressions in String format, we pass it as
       parameter the input.
       2.2 With the eval method (evaluates is expression that we have captured in the parser method).
       2.3 We clean the entry.
       2.4 We insert the result of the eval method.
    3º We create an exception in case the test fails.
    """

    
#Botones / Button
ButtonAC = Button(root, text="AC",width= 15, pady=5, command=clear_display, relief="raised",borderwidth=6, height=1)
ButtonAC.grid(row= 2, column=0)
#------------------------------------------------------------------------ BOTON CONVERTIR /CONVERT BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonConver = Button(root, text="+/-", width= 15,  pady=5, command=lambda:clic_boton("+/-"), relief="raised",borderwidth=6, height=1)
ButtonConver.grid(row= 2, column=1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON TANTO POR CIENTO / BUTTON SO MUCH PERCENT  ----------------------------------------------------------------------------------------------------------------------------------------

ButtonCiento = Button(root, text="%", width= 15, pady=5,command=lambda:clic_boton("%"), relief="raised",borderwidth=6, height=1)
ButtonCiento.grid(row= 2, column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON DIVIDIR / DIVIDE BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonDividir = Button(root, text="/", width= 15,  pady=5, bg="#7C8115", command=lambda:clic_boton("/"), relief="raised",borderwidth=6, height=1)
ButtonDividir.grid(row= 2, column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------ BOTON SIETE / SEVEN BUTTON----------------------------------------------------------------------------------------------------------------------------------------

Buttonsiete = Button(root, text="7",width= 15, pady=5, command=lambda:clic_boton("7"), relief="raised",borderwidth=6, height=1)
Buttonsiete.grid(row= 3, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON OCHO  / EIGHT BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonOcho = Button(root, text="8",width= 15, pady=5,command=lambda:clic_boton("8"), relief="raised",borderwidth=6, height=1)
ButtonOcho.grid(row= 3, column=1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON NUEVE / NINE BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonNueve = Button(root, text="9",width= 15, pady=5, command=lambda:clic_boton("9"), relief="raised",borderwidth=6, height=1)
ButtonNueve.grid(row= 3, column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON MULTIPLICAR / MULTIPLY BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonMult = Button(root, text="*",width= 15,pady=5, bg="#7C8115", command=lambda:clic_boton("*"), relief="raised",borderwidth=6, height=1)
ButtonMult.grid(row= 3, column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON CUATRO / FOUR BUTTON  ----------------------------------------------------------------------------------------------------------------------------------------

ButtonsCuatro = Button(root, text="4", width= 15, pady=5, command=lambda:clic_boton("4"), relief="raised",borderwidth=6, height=1)
ButtonsCuatro.grid(row= 4, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON CINCO / FIVE BUTTON  ----------------------------------------------------------------------------------------------------------------------------------------

ButtonCinco = Button(root, text="5", width= 15,  pady=5, command=lambda:clic_boton("5"), relief="raised",borderwidth=6, height=1)
ButtonCinco.grid(row= 4, column=1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON SEIS / SIX BUTTON  ----------------------------------------------------------------------------------------------------------------------------------------

ButtonSeis = Button(root, text="6", width= 15, pady=5,command=lambda:clic_boton("6"), relief="raised",borderwidth=6, height=1)
ButtonSeis.grid(row= 4, column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON MENOS / MINUS BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonMenos= Button(root, text="-", width= 15, pady=5, bg="#7C8115", command=lambda:clic_boton("-"), relief="raised",borderwidth=6, height=1)
ButtonMenos.grid(row= 4, column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON UNO(/ ONE BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonUno = Button(root, text="1", width= 15,  pady=5,command=lambda:clic_boton("1"), relief="raised",borderwidth=6, height=1)
ButtonUno.grid(row= 5, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON DOS / TWO BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonDos = Button(root, text="2", width= 15, pady=5,command=lambda:clic_boton("2"), relief="raised",borderwidth=6, height=1)
ButtonDos.grid(row= 5, column=1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON TRES / BUTTON THREE ----------------------------------------------------------------------------------------------------------------------------------------

ButtonTres = Button(root, text="3", width= 15,  pady=5,command=lambda:clic_boton("3"), relief="raised",borderwidth=6, height=1)
ButtonTres.grid(row= 5, column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON MAS / MORE BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonMas= Button(root, text="+", width= 15, pady=5,bg="#7C8115", command=lambda:clic_boton("+"), relief="raised",borderwidth=6, height=1)
ButtonMas.grid(row= 5, column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON CERO / ZERO BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonCero = Button(root, text="0",width=36, command=lambda:clic_boton("0"), relief="raised",borderwidth=6, height=1)
ButtonCero.grid(row=6, columnspan=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------ BOTON COMA / COMMA BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

Buttoncoma = Button(root, text=",", width= 15, pady=5,command=lambda:clic_boton(","), relief="raised",borderwidth=6, height=1)
Buttoncoma.grid(row= 6, column=2)
#------------------------------------------------------------------------ BOTON IGUAL / EQUAL BUTTON ----------------------------------------------------------------------------------------------------------------------------------------

ButtonIgual = Button(root, text="=", width= 15,bg="#7C8115", pady=5,command=lambda:calcular(), relief="raised",borderwidth=6, height=1)
ButtonIgual.grid(row= 6, column=3)








root.mainloop()