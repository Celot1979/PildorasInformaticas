import sqlite3

miConexion = sqlite3.connect("BBDD_Curso/GestionPedidos")
miCursor = miConexion.cursor()
misProductos =[
    ("AR01", "CAMISETA", 35, "MODA"),
    ("AR02", "PANTALÓN", 85, "MODA"),
    ("AR03", "COCHE", 75, "JUGUETERIA"),
    ("AR04", "GORRA", 15, "DEPORTES"),
    ("AR05", "PALO GOLF", 240, "DEPORTES")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", misProductos )
miConexion.commit()
miCursor.close()
miConexion.close()