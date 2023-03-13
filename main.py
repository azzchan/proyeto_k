from bs4 import BeautifulSoup
import requests
import re
import datetime
from notifypy import Notify

# print("Bienvenido al gestor de Notifiacion: ")


def request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def link_anime(url):
    url_input = "https://notify.moe{}"
    link = url_input.format(url)
    return link
    
def get_ListName(url):
    soup = request(url)
    anime_web = soup.select("div.explore-anime a img")

    lista_nombres = []
    for img in anime_web:
        name = img.get("alt")
        lista_nombres.append(name)
    return lista_nombres

def get_Name(link):
    animeLink = link_anime(link)
    soup = request(animeLink)
    anime_name = soup.select("div.anime-info h1")
    for name in anime_name:
        anime_name = name.text
    return anime_name

def get_Posicion(list, inputAnime):
    for i in range(len(list)):
        if inputAnime.lower() in list[i].lower():
            posicion = i+1
    return posicion

def get_Link(url, posicion):
    soup = request(url)
    anime_links = soup.select("div.anime-grid-cell a")

    lista_links = []
    for div in anime_links:
        links = div.get("href")
        lista_links.append(links)

    if posicion < len(lista_links):
        return lista_links[posicion-1]

def search_Anime(name,list):
    resultados = []
    for n in list:
        if name.lower() in n.lower():
            resultados.append(n)
    if resultados:
        print(resultados)
    else:
        return None

def get_state_episode(url): # Obtener el estado del espisodio
    animeLink = link_anime(url)
    soup = request(animeLink)
    latest_episode = soup.select("div.episodes a")
    state_episode = "true"
    for episode in latest_episode:
        available = episode.get("data-available")
        span = episode.find("span", class_="episode-title")
        text = span.get_text()
        if available == "true" and text == "-":
            state_episode = "false"
            break
        elif available == "false":
            state_episode = available
            break
    return state_episode

def get_Episode(url): # Numero del espisodio
    animeLink = link_anime(url)
    soup = request(animeLink)
    latest_episode = soup.select("div.episodes a")
    contador = 0
    for episode in latest_episode:
        if episode.get("data-available") != "false": 
            contador += 1
    return contador

    # print(contador)
    
def get_restTime(url):
    animeLink = link_anime(url)
    soup = request(animeLink)
    timer = soup.select("div.episodes a time")
    for datatime in timer:
        timers = datatime.get("datetime")
    print(timers)
    # for episode in timer:
    #     if episode.get("data-available") == "false":
    #         anime_timer = episode.text
            #match = re.search(r'.*(\w{3}, \d{2} \w{3} \d{4})', anime_timer)
            # if match:
            #     date_str = match.group(1)
            #     date = datetime.datetime.strptime(date_str, "%a, %d %b %Y").day
            #     now = datetime.datetime.now().day
            #     time_left = abs(date - now)
            #     print(time_left)

def send_notification(title, message):
    # icon_file = r"icon.ico"
    notification = Notify()
    notification.title = title
    notification.message = message
    # notification.icon = icon_file
    notification.send()

inputAnime = input("¿Cual es el anime ha notificar? \n") # Anime a buscar (input)
url_base = "https://notify.moe/explore" # Pagina Web
Listname = get_ListName(url_base) # Obtenemos la lista de animes

posicion = get_Posicion(Listname,inputAnime) # Buscamos la posicion del anime 
links = get_Link(url_base,posicion) # Obtenemos el link del anime (/anime/id)

anime_name = get_Name(links) # Obtenemos el nombre 
episode_number = get_Episode(links) # Episodio a salir / Ultimo episodio
state = get_state_episode(links) # Estado del espisodio

time = get_restTime(links)
# print(link_anime)


# def main():
#     try:
#         url_base = "https://notify.moe/explore"
#         Listname = get_ListName(url_base)
#         posicion = get_Posicion(Listname,inputAnime)
#         links = get_Link(url_base,posicion) # Link del anime
#         anime_name = get_Name(links)
        
        
        
#         episode_number = get_Episode(links) # Numero episodio a salir
#         state = get_state_episode(links)
        
#         if state == "true":
#             send_notification("Anime Notification", f"El Episodio {episode_number} de {anime_name} está disponible.")
#         else:
#             timer = get_restTime(links)
#             send_notification("Anime Notification", f"El Episodio {episode_number} de {anime_name} no está disponible restan {timer} días.")
#     except requests.exceptions.RequestException as exceptMessage:
#         print("Ocurrió un error al hacer la solicitud GET:", exceptMessage)
    
def send_notification(title, message):
    # icon_file = r"icon.ico"
    notification = Notify()
    notification.title = title
    notification.message = message
    # notification.icon = icon_file
    notification.send()

# main()



