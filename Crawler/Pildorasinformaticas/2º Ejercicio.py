from bs4 import BeautifulSoup
miDoc = """ 
<html>
   <body>
     <p> Este es el primer parrafo</p>

     <p> Este es el segundo parrafo</p>

     <a> es un vinculo</a>




   </body>




</html>


 """

docFinal = BeautifulSoup(miDoc, 'html.parser')

for parrafo in docFinal.find_all("a"):
    print(parrafo.text)
