#salario_base=int(input("Escribe tú salario: "))
h_normales= 8
horas_trabajadas=int(input("Escribe las horas trabajadas: "))
incremento= (h_normales * 20)/100 
h_extra= h_normales * incremento

if horas_trabajadas < 80:
    salario= h_normales * horas_trabajadas
    print("Su salario es: " + str(salario))
elif horas_trabajadas > 80:
    salario = horas_trabajadas * h_extra
    print("Su salario es: " + str(salario))

