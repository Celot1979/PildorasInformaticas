def generarPares(limite):
    num = 1
    numerosPares = []
    while num < limite:
        numerosPares.append(num*2)
        num+=1
    return numerosPares

print(generarPares(6))
