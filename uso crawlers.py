import requests
from bs4 import BeautifulSoup

#Ponemos la web que queremos crawlear
#Usamos r.status_code y si va bien, sale un 200
#Un User-Agent es una cadena de texto que tu navegador (o cliente HTTP) envía al servidor 
# web en cada petición. Sirve para que el servidor sepa qué tipo de cliente eres
# (por ejemplo, Chrome en Windows, Safari en iPhone, un bot de Google, etc.).
#Muchos sitios (como The Verge) bloquean eso porque lo reconocen como un script/bot.
#Por eso, si cambias tu petición para imitar a un navegador real con un User-Agent válido,
# normalmente pasas del 403 a un 200.

html_doc ="""
    <html>
        <body>
            <p> primer párrafo </p>

            <p> segundo párrafo </p>

            <a> vínculo </a>
        </body>
    </html>
 """



headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('https://www.theverge.com/', headers=headers)

print(r.status_code)
print(r.headers)
print(r.encoding)
soup = BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())  # muestra HTML "indented"

for parr in soup.find_all("p"):

    print(parr.text)