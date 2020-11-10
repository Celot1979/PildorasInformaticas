from bs4 import BeautifulSoup
docu = """
<html>

      <style>
        .pImportante{
            color:red;




        }

      </style>
      <body>
         <p class='pImportante'> Este es le primer párrago </p>

          <p> Este es le segundo párrago </p>

          <a>Es un vinculo</a>


      </body>

</html> """

final= BeautifulSoup(docu, "html.parser")
for parrafo in final.find_all("p"):
    print(parrafo.attrs)
    print(parrafo.text)

print(final)