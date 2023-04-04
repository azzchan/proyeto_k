from flask import Flask, request, render_template, session, make_response, redirect
from flask_socketio import SocketIO
from main import get_ListName, get_Posicion, get_AnimeLink, get_Name
from main import get_Episode, get_state_episode, get_restTime, search_Anime
from main import complete_link

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'
socketio = SocketIO(app)

def gestion(anine_name):
    try:
        url_base = "https://notify.moe/explore"
        Listname = get_ListName(url_base)
        position = get_Posicion(Listname,anine_name)
        links = get_AnimeLink(url_base,position)
        anime_name = get_Name(links)
        episode_number = get_Episode(links)
        state = get_state_episode(links)
        time = get_restTime(links, episode_number)
        if state == "false":
            mensaje = f"Episode {episode_number+1} of {anime_name} is avaiable.{time}"
        else:
            mensaje =  f"Episode {episode_number+1} of {anime_name} it`s not avaiable, it`s going to air in {time} days."
        return mensaje
    except:
        return "Hubo un error inesperado"

def obtener_busqueda(name_anime):
    resultados = search_Anime(name_anime, "https://notify.moe/explore")
    return resultados

def obtener_link(busquedas):
    link_animes = []
    for animes in busquedas:
        Listname = get_ListName("https://notify.moe/explore")
        position = get_Posicion(Listname,animes)
        links = get_AnimeLink("https://notify.moe/explore",position)
        link_animes.append(complete_link(links))
    return link_animes

@app.route('/', methods=['GET', 'POST'])
def index():
    busquedas = ""
    link_anime = ""
    show_results = False
    if request.method == 'POST':
        if 'clean_results' in request.form:
            busquedas = ""
            link_anime = ""
        else:
            anime_name = request.form.getlist('anime_input')
            inputAnime = anime_name[0]
            busquedas = obtener_busqueda(inputAnime)
            link_anime = obtener_link(busquedas)
            show_results = True
    return render_template('index.html', show_results=show_results, busquedas=busquedas, links_animes=link_anime)

if __name__ == '__main__':
    app.run(debug=True, port=800)

