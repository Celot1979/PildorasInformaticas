# Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente.
num1=int(input("Introducce el 1ª número: "))
num2=int(input("Introducce el 2ª número: "))
impares=[]
for i in range(num1,num2):
    if i % 2 == 0:
        pares=[]
        #print("Los numero :" + str(i) + " son pares ")
        pares.append(i)
    else:
        #print ("Los numeros: " + str(i) + " son impares ")
        impares.append(i)
        
d = impares[::-1]
print("El orden de los número impares son: " + str(impares))
print("El orden de los número impares descendientes son: " + str(d))