"""Solicitar números al usuario hasta que ingrese el cero. 
Por cada uno, mostrar la suma de sus dígitos (utilizando una función 
que realice dicha suma)."""

def ingresa():
    numeros=[]
    opcion= True

    while opcion == True:
        ingresa= int(input(" Introducce numero: "))
        if ingresa != 0:
            numeros.append(ingresa)
            pass
        elif ingresa == 0:
            numeros.append(ingresa)
            print(sum(numeros))
            opcion == False
            break
    

ingresa()
            