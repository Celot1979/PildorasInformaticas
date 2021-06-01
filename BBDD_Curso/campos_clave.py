import sqlite3

miConexion = sqlite3.connect("BBDD_Curso/GestionPedidos")
miCursor = miConexion.cursor()
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO VARCHAR(40),
        PRECIO INTEGER, 
        SECCION VARCHAR(20)
        )
''')

miConexion.commit()
miCursor.close()
miConexion.close()