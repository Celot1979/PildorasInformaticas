class Persona():
	def hablar(self):
		return "Hablo como una persona"
class Trabajador(Persona):
	def hablar(self):
		return "Hablo como un trabajador"
		
class Director(Trabajador):
	def hablar(self):
		return "Hablo como un director"
		
def hazleHablar(listaDeLasPersonas):
	for persona in listaDeLasPersonas:
		print(persona.hablar())	

        
Antonio=Persona()
Maria=Trabajador()
Ana=Director()
print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())
print("--------------------")
lista=[Antonio,Maria,Ana]

hazleHablar(lista)

		
	