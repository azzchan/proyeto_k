from main import * 

inputAnime = input("What anime is going to be notifiyed? \n") # Anime to search
url_base = "https://notify.moe/explore" # web page

Listname = get_ListName(url_base) # Obtain the naime list
print(Listname)

position = get_Posicion(Listname,inputAnime) # We shearch for the position of the anime
print("posicion:",position)

links = get_AnimeLink(url_base,position) # We obtain the anime link (/anime/id)
print("link:",links)

anime_name = get_Name(links) # We obtain the name
print("anime name:",anime_name)

episode_number = get_Episode(links) # Episode to air / Last espisode
print("espisode number:",episode_number)

state = get_state_episode(links) # Espisode state
print("state:",state)

time = get_restTime(links, episode_number) # Obtain the rest time 
print("time:",time)