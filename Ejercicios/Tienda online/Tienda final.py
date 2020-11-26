Diccionario_frutas = {"platanos": 2, "naranjas": 3, "Peras": 4, "manzanas" : 2.5, "Kiwis": 2.75, "arandanos": 4, "salir": -1}
Diccionario_verduras = {"berenjenas": 2, "coles": 3, "berzas": 4, "acelgas" : 2.5, "repollos": 2.75, "judias": 4, "salir": 0}
Diccionario_carnes = {"pavo": 2, "pollo": 3, "conejo": 4, "aveztruz" : 2.5, "caballo": 2.75, "perdiz": 4, "salir": 0}
Diccionario_pescados = {"merluza": 2, "salmonejos": 3, "gallo": 4, "sardinas" : 2.5, "plateado": 2.75, "salmon": 4, "salir": 0}
lista = []
pedido = 0
frutas = 0
verduras = 0
carnes = 0
pescados = 0
frut = False
ver = False
car = False
pes = False
"""Hubo que añadir a última hora estas variables para que cada opción del menú fuera independiente
Así se puede elegir en el orden que uno desee. """

while len(lista) <= 9:
    c = str(input("Quiere realizar una compra......\n\n1.Fruta\n2.Verduras.\n3.Carnes\n4.Pescados\n ==>  "))
    if c == "1":
        while frutas != 6 and frut== False and len(lista)<= 9:
            #frutas/verduras/carnes/pescado es para pedir sólo hasta 6 productos por catergoria
            #caput en booleano es para que cuando se termine de pedir, se vaya cambiando el valor
            #y deje entrar en la opción de coger la otra categoria
            #El len es para que cuando se lelgue a 10, no se pueda escoger más productos.
            for o,j in Diccionario_frutas.items():
                print("Tenemos las siguiente futas " +" ==> "+ o +" "+ str(j) + " € el kg")
            #Recorremos el diccionario para mostrar por consola las diferentes opciones 
            #de frutas y sus precios.
            try:
                f = str(input("Que fruta desea.....  "))
                lista.append(Diccionario_frutas[f])
                #Sólo se añade a la lista el valor del diccionario, no la clave
                frutas += 1
                pedido += 1
                """Frutas y pedido son variables que su función es que a cada vuelta de bucle cuenten.
                En teoría la de pedido podríamos eliminarla, pues su función era contar para que al llegar 
                a 10 parase el programa.Esa función ahora mismo la está haciendo la función len de la lista """
            
                if f == "salir":
                    lista.pop()
                    """Cuando en el programa deseamos salir en la categoria antes de terminar de elegir
                    los 6 productos, introducciomos la palabra -salir-. Esto lo que nos hace es salir de
                    la elección anterior. Si no usamos el método -pop()- , nos suma un 0; al usar esté método
                    conseguimos que nos quite el último elemento añadido a la lista. El motivo
                    es que tuve que sumár como clave y valor en el diccionario -salir:0- para que no siera error
                    al intentar escribir como elección salir. """
                    print(lista)
                    pedido -= 1
                    frutas -= 1
                    frut = True
            except KeyError:
                print(" Ese producto no se encuentra a su disposición en la tienda, perdone las molestias")
                continue    

    elif c == "2":
        while verduras != 6 and ver== False  and len(lista)<= 9:
            for o,j in Diccionario_verduras.items():
                print("Tenemos las siguientes verduras " +" ==> "+ o +" "+ str(j) + " € el kg")
            try:
                v = str(input("Que verdura desea  "))
                lista.append(Diccionario_verduras[v])
                verduras += 1
                pedido += 1
            
                if v == "salir":
                    lista.pop()
                    print(lista)
                    pedido -= 1
                    verduras -= 1
                    ver = True
            except KeyError:
                print(" Ese producto no se encuentra a su disposición en la tienda, perdone las molestias")
                continue    
    elif c == "3":
        
        while carnes != 6 and car== False  and len(lista)<= 9:
            for o,j in Diccionario_carnes.items():
                print("Tenemos las siguientes carnes " +" ==> "+ o +" "+ str(j) + " € el kg")
            try:
                ca = str(input("Que carne desea  "))
                lista.append(Diccionario_carnes[ca])
                carnes += 1
                pedido += 1
            
                if ca == "salir":
                    lista.pop()
                    print(lista)
                    pedido -= 1
                    carnes -= 1
                    car = True
            except KeyError:
                print(" Ese producto no se encuentra a su disposición en la tienda, perdone las molestias")
                continue    
    elif c == "4":
        while pescados != 6 and pes== False  and len(lista)<= 9:
            for o,j in Diccionario_pescados.items():
                print("Tenemos los siguientes pescados " +" ==> "+ o +" "+ str(j) + " € el kg")
            try:
                p = str(input("Que pescado desea  "))
                lista.append(Diccionario_pescados[p])
                pescados += 1
                pedido += 1
            
                if p == "salir":
                    lista.pop()
                    print(lista)
                    pedido -= 1
                    pescados -= 1
                    pes = True
                
       
        
    else:
        pedido = 10
        break

total = sum(lista)

print("El total que tiene que pagar el cliente es de " + str(total) + "€")
