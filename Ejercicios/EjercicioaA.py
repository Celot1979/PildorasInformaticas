""" Escribe un programa que divida unos alumnos por sexos y por nombre. La clase A serán niñas
con nombre anterior a la M y los niños posterior a la N. Los demás irán a la clase B"""

s= str(input("Eres niño o niña: "))
n= str(input("Cúal es la inicial en Mayùsculas?: "))
lista=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "k", "L","M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lista2=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if s == "niña" or s == "Niña":
    if n in lista:
        if n < "M":
            nom = str(input("¿Cúal es el nombre completo?: "))
            print("La alumna " + nom + " irá a la clase A" )
        elif n > "M":
            nom = str(input("¿Cúal es el nombre completo?: "))
            print("La alumna " + nom + " irá a la clase B" )
    
elif s == "niño" or s == "Niño":
    if n in lista:
        if n > "N":
            nom = str(input("¿Cúal es el nombre completo?: "))
            print("El alumno " + nom + " irá a la clase A" )
        elif n < "N":
            nom = str(input("¿Cúal es el nombre completo?: "))
            print("El alumno " + nom + " irá a la clase B" )
else:
    print("Revise los datos , error")
    

        

