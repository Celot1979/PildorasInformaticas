from bs4 import BeautifulSoup
docu = """
<html>
      <body>
         <p> Este es le primer párrago </p>

          <p> Este es le segundo párrago </p>

          <a>Es un vinculo</a>


      </body>

</html> """

final= BeautifulSoup(docu, "html.parser")
for parrafo in final.find_all("p"):
    print(parrafo.text)

print(final)

