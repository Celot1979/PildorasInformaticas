Diccionario_frutas = {"platanos": 2, "naranjas": 3, "Peras": 4, "manzanas" : 2.5, "Kiwis": 2.75, "arandanos": 4, "salir": 0}
Diccionario_verduras = {"berenjenas": 2, "coles": 3, "berzas": 4, "acelgas" : 2.5, "repollos": 2.75, "judias": 4, "salir": 0}
Diccionario_carnes = {"pavo": 2, "pollo": 3, "conejo": 4, "aveztruz" : 2.5, "caballo": 2.75, "perdiz": 4, "salir": 0}
Diccionario_pescados = {"merluza": 2, "salmonejos": 3, "gallo": 4, "sardinas" : 2.5, "plateado": 2.75, "salmon": 4, "salir": 0}
lista = []
cerrar = True
pedido = 10
frutas = 0
verduras = 0
carnes = 0
pescados = 0
while cerrar:
    if pedido <= 10:
        #Cuando se realiza los pedidos se llega hasta 12 unidades, tienen que ser 10 Cambiar aquí por if pedido == 10: etc. 
        #Luego poner un contador de menos uno en pedidos.
        #Para que cuando llegue a 10 productos se pare
        pr = str(input("Escoge una categoria\n1.Fruta\n2.Verduras.\n3.Carnes\n4.Pescados\n ==>  "))
        if pr == "1":
            while frutas <= 4:
                #Si llega a 5 productos de fruta, saltará al menú principal
                f = str(input("Que fruta desea  "))
                lista.append(Diccionario_frutas[f])
                #Se añade a la lista el valor de la clave del diccionario. Lo que es lo mismo que le precio del producto
                print(lista)
                frutas += 1
                pedido -= 1
                #Se va sumando uno, hasta llegar a 5. Es el contador
                if f == "salir":
                    #Si se teclea en consola salir, directamente se suma 5 al contador y para el bucle.
                    lista.append(Diccionario_frutas[f])
                    frutas += 4
                    pedido -= 1
                    """ Falta por conseguir que al introduccir el - salir- y sumanos su valor, que es cero, no se sume a la lista.
                    Tamién considerar la fórmula de poder borrarlo de la lista, al ser el último elemento """
                    
        elif pr == "2":
            while verduras <= 4:
                v = str(input("Que verdura desea  "))
                lista.append(Diccionario_verduras[v])
                print(lista)
                verduras += 1
                pedido -= 1
                if v == "salir":
                    lista.append(Diccionario_verduras[v])
                    verduras += 4
                    pedido -= 1

        elif pr == "3":
            while carnes <= 4:
                c = str(input("Que carne desea  "))
                lista.append(Diccionario_carnes[c])
                print(lista)
                carnes += 1
                pedido -= 1
                if c == "salir":
                    lista.append(Diccionario_carnes[c])
                    carnes += 4
                    pedido -= 1

        elif pr == "4":
            while pescados <= 5:
                pe = str(input("Que pescado desea  "))
                lista.append(Diccionario_pescados[pe])
                print(lista)
                pescados += 1
                pedido -= 1
                if pe == "salir":
                    lista.append(Diccionario_pescados[pe])
                    pescados += 4
                    pedido -= 1
                    



            
        
    else:
        cerrar = False



print("Terminado y fuera")








    

