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
    soup = request(url)
    anime_names = soup.select("div.explore-anime a img")
    list_names = []
    for get_names in anime_names:
        list_names.append(get_names.get("alt"))
    return list_names

def get_Name(link):
    soup = request(complete_link(link))
    anime_name = soup.select("div.anime-info h1")
    for name in anime_name:
        anime_name = name.text
    return anime_name

def get_Posicion(list, inputAnime):
    for i in range(len(list)):
        if inputAnime.lower() in list[i].lower():
            position = i+1
    return position

def get_AnimeLink(url, position): # Obtain the sought anime link (ex: /anime/asGd86)
    soup = request(url)
    anime_links = soup.select("div.anime-grid-cell a")
    list_links = []
    for gets_links in anime_links:
        list_links.append(gets_links.get("href"))

    if position < len(list_links):
        return list_links[position-1]

def search_Anime(name,list_animes): # Cambiar estructura 
    resultados = []
    for n in list_animes:
        if name.lower() in n.lower():
            resultados.append(n)
    if resultados:
        print(resultados)
    else:
        return None

def get_state_episode(url): # Obtain episode state
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

def get_Episode(url): # Obtain the number of the chapter
    soup = request(complete_link(url))
    latest_episode = soup.select("div.episodes a")
    count = 0
    for episode in latest_episode:
        if episode.get("data-available") != "false":
            count += 1
    return count

def get_restTime(url, episode):
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
    raise ("[187 Error]")
    
def send_notification(title, message):
    # icon_file = r"icon.ico"
    notification = Notify()
    notification.title = title
    notification.message = message
    # notification.icon = icon_file
    notification.send()
    
def main():
    try:
        inputAnime = input("What anime is going to be notifiyed? \n") # Anime to search
        url_base = "https://notify.moe/explore" # web page
        Listname = get_ListName(url_base) # Obtain the naime list
        position = get_Posicion(Listname,inputAnime) # We shearch for the position of the anime
        links = get_AnimeLink(url_base,position) # We obtain the anime link (/anime/id)
        anime_name = get_Name(links) # We obtain the name
        episode_number = get_Episode(links) # Episode to air / Last espisode
        state = get_state_episode(links) # Espisode state
        time = get_restTime(links, episode_number) # Obtain the rest time 
    
        if state == "false":
            send_notification("Anime Notification", f"Episode {episode_number+1} of {anime_name} is avaiable.{time}")
        else:
            send_notification("Anime Notification", f"Episode {episode_number+1} of {anime_name} it`s not avaiable, it`s going to air in {time} days.")
    except requests.exceptions.RequestException as exceptMessage:
        raise("[378 Error]:", exceptMessage)
        
main()
