from notifypy import Notify
from bs4 import BeautifulSoup
import requests

html_crudo = "https://notify.moe/anime/fxRlqPDVR"
resultado = requests.get(html_crudo)
contenido = resultado.text
soup = BeautifulSoup(contenido, "html.parser")


arreglo_elementos = soup.find_all("a", {"data-mountable-type": "episode"})
arreglo_str = [str(i) for i in arreglo_elementos]

contador = 0
string = 'data-available="false"'
for elemento in arreglo_str:
    if string in elemento:
        True
    else:
        contador += 1


nuevo_episodio = arreglo_str[contador]
print(nuevo_episodio)
cadena = 'data-available="true"'
if cadena in nuevo_episodio:
    notification = Notify()
    notification.title = "Anime"
    notification.message = "El anime esta actualmente."
    notification.send()
else:
    print("No ha salido")
