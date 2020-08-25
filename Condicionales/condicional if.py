def evaluacionAlumno(nota):
    valoracion = "aprobado"
    if nota<5:
        valoracion = "suspenso"
    elif nota > 10:
        valoracion = " Nota incorrecta "
    else:
        valoracion = "Aprobado"
    return valoracion
evaluacionAlumno(3)
notaAlumno = int(input(" Introduce la nota: "))

print(evaluacionAlumno(notaAlumno))