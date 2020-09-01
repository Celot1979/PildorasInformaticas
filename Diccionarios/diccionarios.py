las_capitales={"España": "Madrid", "Inglaterra": "Londres", "Portugal": "Lisboa", "Francia": "Paris", "Alemania": "Berlin"}
las_capitales["Italia"] = "Roma"#Añadir
las_capitales["España"]="Oviedo" #Modificar el valor
las_capitales["Asturias"]="Oviedo"

print(las_capitales)
del las_capitales["Asturias"]
print(las_capitales)

#Podemos usar un lista como CLAVe en un diccioario y los valores aposteriori

paises=["España", "Portugal", "Italia", "Francia"]
capitales={paises[0]:"Madrid", paises[1]: "Lisboa", paises[2]:"Roma", paises[3]: "Paris"}
print(capitales)
print(capitales.keys())#Saber las keys/claves
print(capitales.values())#Saber los valores/ values

