import re
nombre1="Carmen Lopez"
nombre2= "Juan Díaz"
nombre3= "sandra Lamuño"

if re.match("Sandra", nombre3, re.IGNORECASE):
    print("He encontrado la persona")
else:
    print("No he encontrado a la persona")


if re.search("Lopez", nombre1):
    print("He encontrado la persona")
else:
    print("No he encontrado a la persona")
    