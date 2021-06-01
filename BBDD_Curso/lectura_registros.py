import sqlite3

miConexion = sqlite3.connect("BBDD_Curso/miBBDD")
miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

muchosProductos = miCursor.fetchall()
for p in muchosProductos:
    print(p)

miCursor.close()
miConexion.close()