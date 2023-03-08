# Proyecto K

HEAD


===

Declaración de responsabilidad, LePravda Group & elif_gang (nosotros en adelante) tenemos conocimiento de los posibles problemas que esto pueda surgir en un futuro al Usuario (usted en adelante) si estos problemas dan como resultado la prohibición al servicio, Nosotros optaremos a suspender el desarrollo/publicación de este Proyecto. Puesto que el operador de
la web la ha diseñado con Usted en mente, su apertura automática mediante un *web scraper* puede suponer un **incumplimiento de las condiciones de uso**. Estas acciones se vuelven especialmente relevantes cuando se accede a grandes volúmenes de información procedente de varias páginas al mismo tiempo o en sucesión rápida, de un modo en el que una persona nunca sería capaz de interactuar con la página. En ningún momento se está tomando datos sensibles,
sí por algún motivo encontramos una brecha de seguridad o vemos que se pueda usar datos sensibles se le notificara inmediatamente al operador de la web.


*Este proyecto está bajo desarrollo, cualquier error que se pueda genera puede contactarnos.*

### Instalación de librerías

---

Para el correcto funcionamiento de esta herramienta se debe tener instalado en su máquina Python en su versión tres además de las siguientes librerías:

* Notify
* BeautifulSoup

```python
pip install notify
pip install beautifulsoup
```

### Changelog

---

v0

* Se moldea la logia inicial.
* Se añade el uso de BeautifulSoup para la obtención de datos de la web.
* Se reacomoda y reescriben todas las variables.

Versión 0.1

* Se vuelve a moldear la logica, ya que se desviaba al objetivo.
* Se añaden nuevas funcionalidades, tales, envio de notificaciones con Notify.
* Se hace uso de Parser para analizar y procesar el codigo fuente en HTML a STR, para su facil manejo.

v0.1.1

* Se elimina el Parser ya que es un proceso demorado e inecesario.
* Se añade más funcionalidades al envio de notificaciones.

v1.0

* Se reconstruye todo el código, ahora manejando metodos.
* Como se elimino Paser, se hace una optención del codigo crudo HTML y se da uso de más funcionalidades de BeautifulSoup.
* Se añaden los primeros metodos `get_latest_espisode` y `send_notificaction`.
* Se crea un metodo llamado `main` que gestionara y llamara metodos necesarios para su correcto funcionamiento.
* Se comienza a usar exepciones para mejorar la obtencion de errores y en consecuencia su arreglo.

v1.1b

* Se testea las funcionalidades y se añade otros metodos de prueba tales como `get_Name` y `get_restTime`.
* Se importa la libreria `re`, ya que a la hora de obtener los atributos de `class` o `id` nos devulve una cadena con caracteres inecesarios.

v1.1.1

* Los metodos de prueba se mantienen. Ahora dandole más funcionalidades al metodo `send_notification`
* Se añade un timer o loop (metodo `main_loop`) para que cada cinco (5) minutos este ejecutando el codigo.
* Se implementa de manera experimental el uso como ejecutable.
* Se añade un icono a las notificaciones.

v1.1.2a

* Para ser el codigo más legible para futuro se ramificara en varios archivos, esto para usar las lineas de codigo adecuadas para un solo metodo.

### Conexión y Obtención de información

---

Para obtener los datos necesarios requerimos de pedirle los datos a la web y lo usaremos usando web scraping, para ello almacenamos la URL que se va a utilizar:

```python
url = "https://notify.moe/anime/fxRlqPDVR"
```

*[https://notify.moe/anime/fxRlqPDVR](https://notify.moe/anime/fxRlqPDVR)* es una web que nos proporciona un indexado de todos los animes que están en transmisión. Además de indicarnos que episodio ya han sido lanzado.

Esta variable esta situada dentro del metodo `main` ya que este sera el que llame y gestione los demás metodos necesarios.

Para las peticiones (requests) usamos el metodo `get_latest_episode` este contendra las llamadas necesarias para obtener toda la información, de la misma hacemos uso de BeautifulSoup para el tratamiento del codigo HTML.

```python
response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
```

En este caso no necesitamos toda la web, solo cierta parte que nos interesa. Para ello pasamos ese contenido por nuestra librería **BeautifulSoup**, para saber más puedes ir a su [documentación](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) oficial.

Gracias a la librería BeautifulSoup podemos usar su función `find_all` que nos ayudara a encontrar toda la información que queramos, actualemte este metodo solo requiere encontrar todas las etiquetas `<a>` que contengan `"data-mountable-type"` y su valor sea `"episode"`.

```python
episode_elements = soup.find_all("a", {"data-mountable-type": "episode"})
```

Anteriormente se usaba Perser para convertir esos elementos HTML a STR para un mejor uso, pero se entendio que no era necesario.

```python
arreglo_str = [str(i) for i in arreglo_elementos]
```

Lo que se hace es que se itera cada etiqueta `<a>` y de ellos tomamos sus valores de `"data-available"`. Si `"data-available"` es false (este false es de HTML y no de Python) cambiara el estado de la variable `latest_episode` y de igualmanera obtenemos el episodio, ya que solo obtenemos los valores true y se detendra si hay un false.

### **Detección de episodios sin ser lanzados**

---

Para detectar cuales son los episodios que no han sido lanzados realizamos un ciclo buscando cada etiqueta `<a>` el estado `"data-available = false"` esto con el fin de ir contando los episodios faltantes. A continuación se dara una condicional

`if available == "true":` si es true colocaremos toda la sintaxis de HTML en `latest_episode` para su posterior tratamiento.

```python
    episode_count = 0
    for episode in episode_elements:
        available = episode.get("data-available")
        episode_count += 1
        if available == "true":
            latest_episode = episode
        else:
            break  
```

Con el contador obtendremos el siguiente capitulo que se lanzara. Así que guardamos y lo retornamos igual que `latest_episode`:

```python
return latest_episode, episode_count
```

Para luego usar estos dos retornos en el metodo `main` que llamara al resto de metodos.

Pero antes, debemos crear la notifiacion con los datos obtenidos que serian `latest_episode` y `episode_count` (numero del episodio) para ello creamos un metodo llamado  `send_notification` y necesitara de un `title` y `message`.

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


Es de tener en cuenta que el metodo `get_latest_episode` necesita url, dada por el metodo `main` y asi mismo llama al metodo `send_notification` y le entrega `title` y `message` de los returns en `get_latest_episode`.

Agregar que el metodo `get_Name` tiene la misma logica, qu `get_latest_episode` solo que este busca una etiqueta `<h1>` y obtiene el el nombre del anime a notificar para darcelo a `main` que gestionara todo despues.

Con el metodo `get_restTime` usa la misma logica a cierto punto, ya que obtiene `"data-available"` para obtener la fecha de lanzamiento para luego calcular cuanto resta para el proximo episodio. Todo ello usando dos librerias `re` y `time`.

## Aclaraciones

Por el momento solo se puede visualizar la notificación si se ejecuta el código en su IDLE de preferencia. Pero se está desarrollando para que sea una aplicación para la computadora y a futuro próximo una web.


elif_gang Developers Group
==========================
