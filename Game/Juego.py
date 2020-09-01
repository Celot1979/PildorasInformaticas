import time 
import random
print("***BIENVENIDOS AL JUEGO DEL CRUZ Y CARA****")
time.sleep(1)


moneda= random.randint(1,2)
moneda2= random.randint(1,2)

opcion1= str(input(" Debes elegir entre ==> ¿CARA O CRUZ?: "))
time.sleep(1)
opcion2= str(input(" Debes elegir entre ==> ¿CARA O CRUZ?: "))
#pregunta =str(input("¿ Desea seguir jugando ?: "))

def jugador(mo, op):
    jugador1=0

    try:
        if op == "cara" or op == "cruz":
            if op == "cara":
                if mo == 1:
                    jugador1+=1
                    print("Ganaste")
                elif mo == 2:
                    print("Perdiste")
            elif op == "cruz":
                if mo == 2:
                    jugador1+=1
                    print("Ganaste")
                elif mo == 1:
                    print("Perdiste")
                

        elif op != "cara" or op != "cruz":
            raise NameError
    except NameError:
        print("Debes elegir entre cara o cruz")
    print(jugador1)
    
def jugador_Dos(mon, opc):
    jugador2=0
    try:
        if opc == "cara" or opc == "cruz":
            if opc == "cara":
                if mon == 1:
                    jugador2+=1
                    print("Ganaste")
                elif mon == 2:
                    print("Perdiste")
            elif opc == "cruz":
                if mon == 2:
                    jugador2+=1
                    print("Ganaste")
                elif mon == 1:
                    print("Perdiste")
        elif opc != "cara" or opc != "cruz":
            raise NameError
    except NameError:
        print("Debe de elegir entre cara y cruz")
    print(jugador2)
    
        
                
#------------------------------------------------------
        
def partida (a,b):
    
    if a == "Ganaste" and b == "Perdiste":
        print ("Gana " + str(a))
    elif a == "Perdiste" and b == "Ganaste":
        print("Gana " + str(b))
    elif a == b:
        print("La moneda está debajo del sofá")
 
            

#jugador(moneda, opcion1)
#jugador_Dos(moneda2, opcion2)

partida(jugador(moneda, opcion1), jugador_Dos(moneda2, opcion2))


#----------------------------


    
 

        
     
    

