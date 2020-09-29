#numeros = int(input("numero: "))
def sumaDigito(numero):
    suma = 0
    suma2= 0
    while numero != 0:
        digito = numero % 10 #Con está operación sacamos el último digito del número 
        #ingresado
        numero = numero//10 #Con esta operación nos daría el primer o primeros
        #digitos del número
        suma = suma + digito
        
    print(suma)
    
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
            print("Los numeros sumados son: ",sum(numeros))
            
            opcion == False
            break
    
ingresa()
sumaDigito(ingresa)

