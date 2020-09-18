# Método Especial __len__()
""" Esté método nos devolvería la longitud de una cadena, lista, tuppla, etc  """
class Agenda():
    def __init__(self):
        self.miAgenda={}

    def agregar_personas(self, nombre, teléfono):
        self.miAgenda[nombre] = teléfono #Clave-valor como cuanquier diccionario  
    def __len__(self):
        return len(self.miAgenda)

agendaPersonal = Agenda()
agendaPersonal.agregar_personas("Dani", "67676767676")  
agendaPersonal.agregar_personas("María", "556565656565")   
print(len(agendaPersonal))#Si intentaramos que nos diera la longitud del diccionario
#Nos dará un error. No debería dar un 2, poque hemos agregado dos contactos.

""" Simplemente por añadir el método __ len __ directamente como método en la clase 
sin cambiar nada más, simplemente añadiendo; nos da el resultado esperado por ter
minal === 2"""