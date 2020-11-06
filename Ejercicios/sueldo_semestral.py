'''Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego: 
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre.'''
calculo_sueldo=[]
for s in range(6):
    sueldo = int(input("Qué sueldos has tenido en los últimos 6 meses: "))
    calculo_sueldo.append(sueldo)

#print(calculo_sueldo)
aguinaldo = sorted(calculo_sueldo, reverse=True)
#print(aguinaldo)
print("Su aguinaldo es de " + str(aguinaldo[0]/2))



