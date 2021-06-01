import sqlite3

miConexion = sqlite3.connect("BBDD_Curso/GestionPedidos_B")
miCursor = miConexion.cursor()
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(40),
        PRECIO INTEGER, 
        SECCION VARCHAR(20)
        )
''')
misProductos =[
    ("CAMISETA", 35, "MODA"),
    ("PANTALÓN", 85, "MODA"),
    ("COCHE", 75, "JUGUETERIA"),
    ("GORRA", 15, "DEPORTES"),
    ("PALO GOLF", 240, "DEPORTES")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", misProductos )
miConexion.commit()
miCursor.close()
miConexion.close()