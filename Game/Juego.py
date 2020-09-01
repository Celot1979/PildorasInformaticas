from time import sleep
import random
jugador1=0
jugador2=0
moneda= random.randint(1,2)
pr = str(input("Cara o Cruz: ==>"))
def jugador_uno(pregunta):
    if pregunta == "Cara":
        print("Ganaste")
    elif pregunta == "Cara":
        print("Perdiste")
    elif pregunta == "Cruz":
        print("Ganaste")
    elif pregunta == "Cruz":
        print("Perdiste")
    
    

jugador_uno(pr)