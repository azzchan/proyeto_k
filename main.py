from notifypy import Notify
from bs4 import BeautifulSoup
import requests
import re
import datetime
import time


def main():
    url = "https://notify.moe/anime/fxRlqPDVR"
    try:
        latest_episode = get_latest_episode(url)
        if latest_episode == "true":
            timer = get_restTime(url)
            name_anime = get_Name(url)
            episode_number = latest_episode[1]
            send_notification("Anime Notification", f"El Episodio {episode_number} de {name_anime} está disponible.")
        else:
            timer = get_restTime(url)
            name_anime = get_Name(url)
            episode_number = latest_episode[1]
            send_notification("Anime Notification", f"El Episodio {episode_number} de {name_anime} no está disponible restan {timer} días.")
    except requests.exceptions.RequestException as exceptMessage:
        print("Ocurrió un error al hacer la solicitud GET:", exceptMessage)

def get_restTime(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    timer = soup.find_all("a", {"data-available": "false"})

    for episode in timer:
        if episode.get("data-available") == "false":
            anime_timer = episode.text
            match = re.search(r'.*(\w{3}, \d{2} \w{3} \d{4})', anime_timer)
            if match:
                date_str = match.group(1)
                date = datetime.datetime.strptime(date_str, "%a, %d %b %Y").day
                now = datetime.datetime.now().day
                time_left = abs(date - now)
                return time_left
        
def get_Name(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    episode_name = soup.find_all("h1", {"data-mountable-type": "header"})
    for episode in episode_name:
        anime_name = episode.text
    return anime_name

def get_latest_episode(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    episode_elements = soup.find_all("a", {"data-mountable-type": "episode"})
    latest_episode = "true"
    episode_count = 0
    for episode in episode_elements:
        available = episode.get("data-available")
        episode_count += 1
        if available == "true":
            latest_episode = episode
        else:
            break  
    return latest_episode, episode_count

def send_notification(title, message):
    # icon_file = r"icon.ico"
    notification = Notify()
    notification.title = title
    notification.message = message
    # notification.icon = icon_file
    notification.send()

def main_loop(tiempo_espera):
    while True:
        main()
        time.sleep(tiempo_espera)
        
if __name__ == "__main__":
    tiempo_espera = 15 
    main_loop(tiempo_espera)
