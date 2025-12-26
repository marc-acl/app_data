import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

docPage = requests.get("https://python.beispiel.programmierenlernen.io/")

finalDoc = BeautifulSoup(docPage.text, "html.parser")

#emoji es un estilo en la web
#imprime todos los emoji
print(finalDoc.select(".emoji"))

#también podemos imprimir por elementos
emojis = finalDoc.select(".emoji")
print(emojis[0].text)

#Traemos el texto Polarised modular conglomeration
titulo = finalDoc.select(".card-title")
print(titulo[0].text)

#Traemos el párrafo Optio numquam...
#parrafo = finalDoc.select(".card-text")
#otra forma
parrafo = finalDoc.select(".card-text")
print(parrafo)

#Traemos la imagen del bloque
imagen = finalDoc.select(".card-block img")
print(imagen[0])

print("*****************************************************")
urlBase = "https://python.beispiel.programmierenlernen.io/"
#también podemos recorrer con un bucle
#sacamos todo el bloque
#urljoin es para unir dos url
#así damos con la url de la imagen
bloque = finalDoc.select(".card-block")
for i in range(len(bloque)):
    #print(emojis[i].text)
    print("")
    print(titulo[i].text)
    print("")
    print(parrafo[i].text)
    print("")
    print(urljoin(urlBase, imagen[i].attrs["src"]))
    print("")

#imprimir los emojis
for i in emojis:
    print(i.text)

#profundizar en vínculos
vinculo = finalDoc.select(".navigation .btn")[0].attrs["href"]
print(urljoin(urlBase, vinculo))
