from bs4 import BeautifulSoup
miDoc = """ 
<html>
   
   <style>
    .pImportante{

        color:red;
    }

   </style>


   
   <body>
     <p class ='pImportante'> Este es el primer parrafo</p>

     <p> Este es el segundo parrafo</p>

     <a> es un vinculo</a>




   </body>




</html>


 """

docFinal = BeautifulSoup(miDoc, 'html.parser')

for parrafo in docFinal.find_all("p"):
    print(parrafo.attrs)
    print(parrafo.text)
