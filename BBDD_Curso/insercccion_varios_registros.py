import sqlite3

miConexion = sqlite3.connect("BBDD_Curso/miBBDD")
miCursor = miConexion.cursor()
muchosProductos =[
    ("Patin", 100, "Deportes"),
    ("Cenicero", 20, "Cerámica"),
    ("Pantalón", 80, "Moda")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", muchosProductos)
miConexion.commit()





miCursor.close()
miConexion.close()
