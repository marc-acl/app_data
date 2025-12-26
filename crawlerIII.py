#profundizar en vínculos
import requests
import csv
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
import time

inicio = time.time()

urlBase = "https://python.beispiel.programmierenlernen.io/"
 
#Escribimos la información obtenida en un csv
#excel separa por columnas cuando ve ;

print("*****************************************Home*************************************************")

#debe envolver el bucle siempre
with open('ausflistung.csv', 'w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["Emoji", "Título", "Párrafo", "Imageb"])
    
    #contador =0
    while urlBase !="":

        docPage = requests.get(urlBase)

        finalDoc = BeautifulSoup(docPage.text, "html.parser")

        #Traemos el emoji
        emojis = finalDoc.select(".emoji")

        #Traemos el texto Polarised modular conglomeration
        titulo = finalDoc.select(".card-title span")

        #le damos una espera de 2 segundos a cada petición
        time.sleep(2)

        #Traemos el párrafo Optio numquam...
        #parrafo = finalDoc.select(".card-text")
        #otra forma
        parrafo = finalDoc.select(".card-text")

        #Traemos la imagen del bloque
        imagen = finalDoc.select(".card-block img")

        #otra forma del for, así me trae cada elemento card con un i
        #select_one selecciona el primer elemento
        bloque = finalDoc.select(".card")
        for i in bloque:
            print(i.select_one(".emoji").text)
            print(i.select(".card-title span")[1].text)
            print(i.select_one(".card-text").text)
            print(urljoin(urlBase, i.select_one("img").attrs["src"]))
            emoji = i.select_one(".emoji").text
            titles = i.select(".card-title span")[1].text
            parrs = i.select_one(".card-text").text
            imagenUurl = urljoin(urlBase, i.select_one("img").attrs["src"])
            print("")
            #contador += 1
            spamwriter.writerow([emoji, titles, parrs, imagenUurl])

        

        #también puedo usar un if
        try:
            #vinculo tiene index.php?page=2 y lo une con la url base, si da error es porque no exite
            vinculo = finalDoc.select(".navigation .btn")[0].attrs["href"]
            parsed = urlparse(vinculo)
            query_params = parse_qs(parsed.query)
            pageNumber = query_params["page"][0]
            urlBase = urljoin(urlBase, vinculo)
            print("*********************************Page ", pageNumber,"*************************************")
        except IndexError:
            #así salimos del while
            urlBase = ""

        

fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")




    

    
