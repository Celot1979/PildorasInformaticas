import sqlite3

miConexion = sqlite3.connect("BBDD_Curso/miBBDD")
miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

muchosProductos = miCursor.fetchall()
print(muchosProductos)

miCursor.close()
miConexion.close()