
d = {"platanos":2, "manzanas": 3, "arandanos": 4, "ciruelas" : 2.45, "peras": 2, "dactiles": 4.56, "mangos": 5, "paraguayos": 4.5, "mandarinas": 3, "aguacates": 3.75, "continua": 0 }
d_Dos = {"lechugas":2, "coles": 3, "": 4, "alcachofas" : 2.45, "nabos": 2, "acelgas": 4.56, "berzas": 5, "navizas": 4.5, "brocoli": 3, "repollo": 3.75 }
d_Tres = {"perdiz":2, "conejo": 3, "pollo": 4, "avestruz" : 2.45, "ciervo": 2, "cerdo": 4.56, "ternera": 5, "jabali": 4.5, "entrecot": 3, "": 3.75 }
lista=[]


def fruta():
    fruta=6
    cantidad = 0
    pregunta = str(input("Desea comprar fruta?"))
    if pregunta == "si":
        for f,p in d.items():
            print("Tienes para elegir " + f + " con un precio de "+ str(p) + " €")
        print("En su compra de fruta tiene un máximo de 6 productos")
        maximo = 0
        while maximo != 6:
            producto= str(input("Que producto:"))
            lista.append(d[producto])
            maximo+=1
            


            if producto == "continua":
                maximo+=6
                print("Continuamos")
            
                break
            elif pregunta != "si":
                maximo = 6
            
            
        return lista
        
        
            
       
    




while len(lista) < 10:
    fruta()
    print(lista)


"""Pendiente:
1º que cada elemento cuente tanto dentro de la función como fuera . Es decir, que cuente como uno de los 6 dentro de la lsita como uno de los 10 en total
2º No salta - continua - en verdura y carne
3º Tendriamos que poder pasar en la 1º elección si quisieramos.
4º  Al crear una única lista con los precios de los productos, tendria que sumarse y generar un escrito con el total"""


