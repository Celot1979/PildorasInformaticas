lista=["Hello","How","Are", "you"]
resultado=[]
for i in lista:
    resultado.append(i[0:2])
print("".join(resultado))