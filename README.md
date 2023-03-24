
![Banner](https://i.ibb.co/BZL0WFT/proyecto-k.png)
[![v1.1.2b](https://img.shields.io/badge/release-v1.1.2b-green)](https://github.com/azuzu0/proyeto_k/blob/main/log/v1.1.2b/README.md)
# Proyecto K

Declaración de responsabilidad, LePravda Group & elif_gang (nosotros en adelante) tenemos conocimiento de los posibles problemas que esto pueda surgir en un futuro al Usuario (usted en adelante) si estos problemas dan como resultado la prohibición temporal o permanente del servicio. Nosotros optaremos a suspender el desarrollo/publicación de este Proyecto. Puesto que el operador de la web la ha diseñado con Usted en mente, su apertura automática mediante un *web scraper*  puede suponer un **incumplimiento de las condiciones de uso**. Estas acciones se vuelven especialmente relevantes cuando se accede a grandes volúmenes de información procedente de varias páginas al mismo tiempo o en sucesión rápida, de un modo en el que una persona nunca sería capaz de interactuar con la página. En ningún momento se está tomando datos sensibles,
sí por algún motivo encontramos una brecha de seguridad o detectanos que se pueda usar datos sensibles se le notificara inmediatamente al operador de la web.

*Este proyecto está bajo desarrollo, cualquier error que se pueda genera puede contactarnos.*

*[Notify.moe](https://notify.moe/)* es una web que nos proporciona un indexado de todos los animes que están en transmisión. Además de indicarnos que episodio ya han sido lanzado. Puede revisar su repositorio en [Github](https://github.com/animenotifier/notify.moe).
## Requisitos

Para el correcto funcionamiento de esta herramienta se debe tener instalado en su máquina Python en su versión tres además de las siguientes librerías:

```python
    pip install notify
    pip install beautifulsoup
```
Tambien se requiere de otras librerias ya propias de Python 3, tales como:
```python
    import requests
    import re
    import datetime
```
## Funciones
    
* Tiene la capacidad de buscar el Anime que este en la base de datos.
* Obtendra una notificacion pop-up en Windows con el nombre y episodio, tambien el tiempo restante si no ha salido.
## Hoja de Ruta

- Mostrar la notificacion vía Web.

- Realizar la busqueda del Anime vía Web.

- Mostrar una parilla con todos los animes disponibles.


## Documentación

Para obtener los datos necesarios requerimos de pedirle los datos a la web y lo usaremos usando web scraping, para ello almacenamos la URL que se va a utilizar:

```python
url_base = "https://notify.moe/"
```

Esta variable esta situada dentro del metodo `main` ya que este sera el que llame y gestione los demás metodos necesarios.

Para las peticiones (requests) usamos el metodo `request` este contendra las llamadas necesarias para obtener toda la información, de la misma hacemos uso de BeautifulSoup para el tratamiento del codigo HTML.

```python
def request(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup
```

En este caso no necesitamos toda la web, solo cierta parte que nos interesa. Para ello pasamos ese contenido por nuestra librería **BeautifulSoup**, para saber más puedes ir a su [documentación](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) oficial.

Gracias a la librería BeautifulSoup podemos usar su función `select` que nos ayudara a encontrar la información que queramos de la manera más presisa posible, a continuación un fracmento del uso que se le esta dando actualemte. En esta linea buscamos los `div` que contengan las clases con valores `explore-anime`, luego entramos a los etiquetas `a` y luego la etiqueta `img`.

```python
anime_names = soup.select("div.explore-anime a img")
```
Nota de [azuzu0](https://github.com/azuzu0): 
Anteriormente se usaba Perser para convertir algunos  elementos HTML a STR para un mejor uso, pero se entendio que no era necesario.

```python
arreglo_str = [str(i) for i in arreglo_elementos]
```

Ahora solamente usamos un ciclo donde recorre todos los `img` que contiene en este caso los nombres de anime y los almacenamos en un vector para su posterior uso.

```python
   list_names = []
    for get_names in anime_names:
        list_names.append(get_names.get("alt"))
    return list_names
```


**Detección de episodios sin ser lanzados**

Para detectar cuales son los episodios que no han sido lanzados realizamos un ciclo buscando cada etiqueta `a` en los `div` con un valor en su clase de `episodes`, luego obtendremos su `data-available` y realizamos un conteo de ello. Además de que si
`if episode.get("data-available") != "false":` nos devuelve un diferente de "false" este aumentara el valor del conteo.

```python
    for episode in latest_episode:
        if episode.get("data-available") != "false":
            count += 1
```

Con el contador obtendremos el siguiente capitulo que se lanzara. Así que guardamos y lo retornamos.

**Notifiación**

Para crear la notifiacion con los datos obtenidos de los metodos tales como `get_Episode` `get_Namey` y `get_restTime`para ello creamos un metodo llamado  `send_notification` y necesitara de un `title` y `message`.

```python-repl
def send_notification(title, message):
    icon_file = r"icon.ico"
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.icon = icon_file
    notification.send()
```

Expliquemos un poco el funcionamiento de la notificación. Para ello creamos una variable donde contendrán el método **Notify()**, ya con ello listo nos dará la posibilidad de usar varias funciones. La que vamos a usar son *.title* para el título de la notificación, *.message* para el mensaje en cuestión y ya por ultimo *.send()* para hacer efectivo la visualización.


## Aclaraciones

Por el momento solo se puede visualizar la notificación si se ejecuta el código en su IDLE de preferencia. Pero se está desarrollando para que sea una aplicación para la computadora y a futuro próximo una web.

## Chnagelogs

[![v0](https://img.shields.io/badge/changelog-v0-orange)](https://github.com/azuzu0/proyeto_k/blob/main/log/v0/README.md)

[![v0.1](https://img.shields.io/badge/changelog-v0.1-orange)](https://github.com/azuzu0/proyeto_k/tree/main/log/v0.1/README.md)

[![v0.1.1](https://img.shields.io/badge/changelog-v0.1.1-orange)](https://github.com/azuzu0/proyeto_k/blob/main/log/v0.1.1/README.md)

[![v1.0](https://img.shields.io/badge/changelog-v1.0-orange)](https://github.com/azuzu0/proyeto_k/blob/main/log/v1.0/README.md)

[![v1.1.1](https://img.shields.io/badge/changelog-v1.1.1-orange)](https://github.com/azuzu0/proyeto_k/blob/main/log/v1.1.1/README.md)

