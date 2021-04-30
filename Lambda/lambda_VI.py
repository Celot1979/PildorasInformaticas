"""Ordena la lista de música alfabeticamente
1º con función y luego con lambda """
musico=["Paul McCartney", "Bruce Springstee", "Tina Turner", "Justin Bieber", "Elthon John"]

"""def ordena_musicos(m):
    return m.split()[0]

musico.sort(key=ordena_musicos)
print(musico)"""

musico.sort(key=lambda m :m.split()[0])
print(musico)
