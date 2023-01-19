import socket
import sys

objetivo = socket.gethostbyname(input("Inserte la dirección Ip : "))
print("Escaneando puertos ....." + objetivo)

try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print("El puerto {} está abierto".format(port))
        s.close()
except:
    print("\n saliendo ...." )
    sys.exit(0)