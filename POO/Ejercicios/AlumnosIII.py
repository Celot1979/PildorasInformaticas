class cls_Alumno:
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido= apellido
        self.lst_notas = []
    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()}"

    def pon_nota(self, arg_int_nota):
        if 0 <= arg_int_nota <= 10:
            self.lst_notas.append(arg_int_nota)

    def nota_media(self):
        return round(sum(self.lst_notas) / len(self.lst_notas),3)

    def imprime_ficha(self):
        print(self)
        for i, nota in enumerate(self.lst_notas):
            print(f"{i} .- {nota}")
        print(f"\n Promedio: {self.nota_media()}")

    def cmp_nombre(self,arg_obj_alumno):
        return (self.apellido + self.nombre) < (arg_obj_alumno.apellido + arg_objalumno.nombre)

    def cmp_notas(self,arg_obj_alumno):
        return(self.nota_media()) < arg_obj_alumno.nota_media()







if __name__ == "__main__":
    obj_alumno = cls_Alumno("luis", "urbalejo")
    print(obj_alumno)
    obj_alumno.pon_nota(8)
    obj_alumno.pon_nota(7)
    obj_alumno.pon_nota(10)
    obj_alumno.imprime_ficha()
    lst_alumnos = []
    lst_alumnos.append(obj_alumno)

if __name__ == "__main":
    lst_clase = []
    obj_alumno = cls_Alumno("Luis", "Urballejo") ; lst_clase.append(obj_alumno)
    obj_alumno = cls_Alumno("Rodigo", "Cabrera") ; lst_clase.append(obj_alumno)
    obj_alumno = cls_Alumno("Paola", "Franco") ; lst_clase.append(obj_alumno)
    obj_alumno = cls_Alumno("Cesar", "Aguas") ; lst_clase.append(obj_alumno)
    obj_alumno = cls_Alumno("Teff", "Matt") ; lst_clase.append(obj_alumno)
    #Vamos a agregarle notas aleatorias
    import random
    for obj_alumno in lst_clase:
        for i in range(4):#pondremos 4 calificaciónes
            obj_alumno.pon_nota(random.randint(0,10))

    #Ordena la clase por orden alfabético
    # Ordenaremos la lista con el método de odisea burbujas
    for ind1 in range(len(lst_clase)-1):
        for ind2 in range(ind1+1, len(lst_clase)):
            if not lst_clase[ind1].cmp_nombre(lst_clase[ind2]):
                lst_clase[ind1], lst_clase[ind2] = lst_clase[ind2], lst_clase[ind1]
    print("\nALUMNOS ORDENADOS POR APELLIDO, NOMBRE: ")
    for obj in lst_clase: print(obj)
    #Ordena la clase por nota media
    for ind1 in range(len(lst_clase)-1):
        for ind2 in range(ind1+1,len(lst_clase)):
            if lst_clase[ind1].cmp_notas(lst_clase[ind2]):
                lst_clase[ind1], lst_clase[ind2] = lst_clase[ind2], lst_clase[ind1]
                
    print("\nALUMNOS ORDENADOS POR NOTA MEDIA: ")
    for obj in lst_clase:  print(obj, obj.nota_media())
                
    


   
    


    