import re
# Metodos Start, end y span
cadena ="Estoy trabajando con Python el Martes y Semana Santa"
print(re.search("Estoy", cadena))
busqueda ="Martes"
texto_encontrado =re.search(busqueda, cadena)
print(texto_encontrado.start())
""" Lo que se busca es realizar primero 
una varible que cree la busqueda principal 
con su  patrón y su cadena donde buscar.
Luego se usa el método start para saber donde
comienza esa palabra que buscamos en el texto,
que en esté caso está en la variable
busqueda"""
print(texto_encontrado.end())
""" La finalidad es pareciada al anterior.
Salvo porque no dirá donde está el final
de la busqueda""" 

print(texto_encontrado.span())
""" En caso que deseemos hacer las dos acciones
anteriores a la vez, usamos esta función"""