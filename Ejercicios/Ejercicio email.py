"""Nos mandan hacer un programa que verifiquen si la dirección de email 
introduccida por el usario es correcta o incorrecta"""

email = str(input(" introduce el email: "))
try:
    if "@" in email and ".com" in email:
        print("Dirección correcta")
    else:
        print("dirección incorrecta")

except:
    print("algo ha pasado")