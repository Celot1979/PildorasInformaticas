import requests
miReq = requests.get('https://www.movistar.es')

# print(miReq.status_code) 
""" Está insturcción es para saber si la
peticion ha quedado correctamente ejecutada. """

# print(miReq.headers)
""" Está otra sentencia es para obtener información adicional. """

print(miReq.text) 
""" Con está sentencia lo que veremos es el código HTML
de toda la página pasada a texto """