import random
numero_aleatorio = random.randint(0,100)
print (numero_aleatorio)
cont = 0
usuario = int(input(" Escribe un número \n"))
acierto = True

while acierto == True:
    if numero_aleatorio == usuario:
        cont += 1
        if cont == 1:
             print ("Correcto. Has utilizado… " + str(cont) + " sólo intento ")
        else:
             print ("Correcto. Has utilizado… " + str(cont) + " nº de intentos consumidos ")
        acierto = False
    else:
        if(numero_aleatorio < usuario):
            print("El número introduccido es mayor que el aleatorio ")
            cont += 1
            usuario = int(input(" Escribe otro número \n"))
        elif (numero_aleatorio > usuario):
            print("El número introduccido es menor que el aleatorio ")
            cont +=1
            usuario = int(input(" Escribe otro número \n"))
    