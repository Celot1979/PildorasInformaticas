import sqlite3

miConexion = sqlite3.connect("BBDD_Curso/miBBDD")
miCursor = miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS(NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('CAMISETA',25, 'MODA')")
#Cada vez que se realice un cambio en una BBDD con alguna instrucción de
#se debe de confirmar con esta instrucción.
miConexion.commit()





miCursor.close()
miConexion.close()
