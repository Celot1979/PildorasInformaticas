Diccionario_frutas = {"platanos": 2, "naranjas": 3, "Peras": 4, "manzanas" : 2.5, "Kiwis": 2.75, "arandanos": 4}
lista = []
fr= 0

for v in range (10):
    d = str(input("Que producto quieres: \n1.Frutas\n2.Verduras\n3.Carne\nPescado\n==>"))
    if d == "1":
        f = str("Vamos hacer la lista de la fruta: ")
        while f != "Termine":
            if fr != 6:
                fruta = str(input("Que fruta deseas: "))
                lista.append(Diccionario_frutas[fruta])
                fr+=1
                if fruta == "termine":
                    break
            else:
                print("Gracias por su compra")


            


print(lista)










    

