print("Programa de cálculo de tipo impositico en RENTA 2020: ")
renta = int(input("Introducce tu RENTA: "))
tipo = 0
if renta <= 12000:
    tipo=7
elif 12000<renta<18000:
    tipo=15
elif 18000<renta<35000:
    tipo=21
elif 350000<renta<700000:
    tipo=35
else:
    tipo=45
print("A la renta" + str(renta) + "le corresponde un " + str(tipo) + "% tipo impositivo")

    



