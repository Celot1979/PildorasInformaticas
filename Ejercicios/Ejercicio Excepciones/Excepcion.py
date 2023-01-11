nombrePersonas =[]
def agregar(lista, nombreIntroducido):
    try:
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(nombreIntroducido)
    except ValueError:
        print("Error: %s" % nombreIntroducido + " repetido")



cont = 1
while cont < 11:
    nombre = str(input("Introduccir nombre : " + "\n"))
    agregar(nombrePersonas,nombre)
    cont +=1 
