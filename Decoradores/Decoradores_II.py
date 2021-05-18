def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args, **kwargs):
        print("A continuación voy hacer un cálculo")
        funcion_parametro(*args, **kwargs)
        print("Ya he terminado el trabajo")

    return funcion_interna()


@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

potencia(base=5,exponente=3)

