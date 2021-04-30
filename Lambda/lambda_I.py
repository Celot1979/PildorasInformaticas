""" Para comenzar a entender las funciones 
Lambda , empezaremos viendo un 
ejemplo del cálculo de un area de un triángulo."""

"""def area(b,a):
    a = (b*a)/2
    return a

triangulo1 = area(2,3)
triangulo2 = area(4,4)"""
#Hemos crado una función ordinaria con la
#con simple código. Es ídonea para 
#pasarla a funcion lambda

area_triangulo= lambda base,altura:(base*altura)/2


print(area_triangulo(3,6))
print(area_triangulo(15,25))