def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        print("A continuación voy hacer un cálculo")
        funcion_parametro()
        print("Ya he terminado el trabajo")

    return funcion_interna




@funcion_decoradora
def sumar():
    print(35 + 30)

@funcion_decoradora
def resta():
    print(30-25)

sumar()
resta()

