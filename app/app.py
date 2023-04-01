from flask import Flask, request, render_template, session
from main import get_ListName, get_Posicion, get_AnimeLink, get_Name, get_Episode, get_state_episode, get_restTime
app = Flask(__name__)

def gestion(anine_name):
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vals = request.form.getlist('values')
        test = vals[0]
        respuesta = gestion(test)
    else:
        respuesta = ""
    # session.clear()
    return render_template('index.html', result=respuesta)

if __name__ == '__main__':
    app.run(debug=True, port=800)

