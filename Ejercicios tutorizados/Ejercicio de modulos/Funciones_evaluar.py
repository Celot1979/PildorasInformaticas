def usuario():
    user = str(input("Introducce tu usuario:\n==>"))
    if len(user) < 5:
        print("El usuario no puede tener menos de 5 caracteres")
    elif len(user) > 15:
        print ("El usuario no puede tener más de 15 caracteres")
    elif user.isalnum() != True:
        print("El usuario solo puede contener letras y números")
    else:
        print("Usuario correcto")


def passw():
    mayusculas = False
    mayu = 0
    min = 0
    minusculas = False
    espacio = 0
    letras_numeros = 0
    caracater_No_Caracter = 0
    no_numero= False
    validar = False

    p= str(input("Introducce la contraseña\n==>"))
    cantidad = len(p)
    if cantidad < 10:
        print("La contraseña debe ser mayor de 10 caracteres")
    if p.isalnum() == False:
        letras_numeros += 1
        if letras_numeros == 0:
            print("La contraseña debe contener un carácter que no sea ni letra ni número")
        for c in p:
            if c.isupper() == True:
                mayu += 1
                if mayu > 0:
                    mayusculas = True
                else:
                    print("Contraseña insegura - Al menos debe de tener una minuscula -")
            elif c.islower() == True:
                min += 1
                if min > 0:
                    minusculas = True
                if min == 0:
                    print("Contraseña insegura - Al menos debe de tener una mayuscula -")
        
            elif c.isspace() == True:
                espacio += 1
                if espacio == 0:
                    print("Correcto")
                else:
                    print("La contraseña no puede tener espacios")
    
    if mayu > 0 and min > 0 and letras_numeros > 0:
            if espacio >= 1:
                print("Incorrecto")
            
            elif mayu == 0:
                print("Contraseña insegura - Al menos debe de tener una minuscula -")
            elif min == 0:
                print("Contraseña insegura - Al menos debe de tener una mayuscula -")
            elif espacio > 0:
                print("La contraseña no puede tener espacios")
            else:
                print("CORRECTO")   






