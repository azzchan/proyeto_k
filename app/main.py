from bs4 import BeautifulSoup
import requests
import re
import datetime
from notifypy import Notify


def request(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup

def complete_link(url): # We return the complete link
    url_input = "https://notify.moe{}".format(url)
    return url_input

def get_ListName(url):
    try:
        soup = request(url)
        anime_names = soup.select("div.explore-anime a img")
        list_names = []
        for get_names in anime_names:
            list_names.append(get_names.get("alt"))
        return list_names
    except:
        return "Error 40: Fallo al obtener la lista de animes."

def get_Posicion(list_animes, inputAnime):
    try:
        position = None
        for i in range(len(list_animes)):
            if inputAnime.lower() in list_animes[i].lower():
                position = i+1
        if position is None:
            raise ValueError
        return position
    except TypeError:
        return "Error 11: El dato ingresado no es de tipo string."
    except:
        return "Error 41: Fallo al encontrar el anime"

def get_AnimeLink(url, position): # Obtain the sought anime link (ex: /anime/asGd86)
    try:
        soup = request(url)
        anime_links = soup.select("div.anime-grid-cell a")
        list_links = []
        for gets_links in anime_links:
            list_links.append(gets_links.get("href"))
        return list_links[position-1]
    except:
        return "Error 42: Fallo al obtener el link del anime."

def get_Name(link):
    try:
        soup = request(complete_link(link))
        anime_name = soup.select("div.anime-info h1")
        for name in anime_name:
            anime_name = name.text
        return anime_name
    except:
        return "Error 43: Fallo al obtener el nombre."
    
def get_Episode(url): # Obtain the number of the chapter
    try:
        soup = request(complete_link(url))
        latest_episode = soup.select("div.episodes a")
        count = 0
        for episode in latest_episode:
            if episode.get("data-available") != "false":
                count += 1
        return count
    except:
        return "Error 44: Fallo al obtener el episodio."

def get_state_episode(url): # Obtain episode state
    try:
        soup = request(complete_link(url))
        latest_episode = soup.select("div.episodes a")
        state_episode = "true"
        for episode in latest_episode:
            available = episode.get("da a-available")
            span = episode.find("span", class_="episode-title")
            if available == "true" and span.get_text() == "-":
                state_episode = "false"
                break
            elif available == "false":
                state_episode = available
                break
        return state_episode
    except:
        return "Error 45: Fallo al obtener el estado del episodio."

def get_restTime(url, episode):
    try:
        soup = request(complete_link(url))
        timer = soup.select("div.episodes a")
        dates = []
        for datatime_anime in timer:
            dates.append(datatime_anime.text)
        match = re.search(r'.*(\w{3}, \d{2} \w{3} \d{4})', dates[episode])
        if match:
            date_str = match.group(1)
            date = datetime.datetime.strptime(date_str, "%a, %d %b %Y")
            now = datetime.datetime.now()
            date1 = datetime.date(date.year, date.month, date.day)
            date2 = datetime.date(now.year, now.month, now.day)
            daysLeft = abs(date2 - date1)
            return daysLeft.days
    except:
        return "Error 46: Fallo al obtener el tiempo restante."

def search_Anime(name,list_animes): # Cambiar estructura 
    resultados = []
    for n in list_animes:
        if name.lower() in n.lower():
            resultados.append(n)
    if resultados:
        return resultados
    else:
        return None

def send_notification(title, message):
    icon_file = r"imagen.jpeg"
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.icon = icon_file
    notification.send()

