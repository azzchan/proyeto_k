# Anime Notifier

Declaración de responsabilidad, LePravda Group & Azuzu Developers (nosotros en adelante) tenemos conocimiento de los posibles problemas que esto pueda surgir en un futuro al Usuario (usted en adelante) si estos problemas dan como resultado la prohibición al servicio, Nosotros optaremos a suspender el desarrollo/publicación de este Proyecto. Puesto que el operador de
la web la ha diseñado con Usted en mente, su apertura automática mediante un *web scraper* puede suponer un **incumplimiento de las condiciones de uso**. Estas acciones se vuelven especialmente relevantes cuando se accede a grandes volúmenes de información procedente de varias páginas al mismo tiempo o en sucesión rápida, de un modo en el que una persona nunca sería capaz de interactuar con la página. En ningún momento se está tomando datos sensibles,
sí por algún motivo encontramos una brecha de seguridad o vemos que se pueda usar datos sensibles se le notificara inmediatamente al operador de la web.

*Este proyecto está bajo desarrollo, cualquier error que se pueda genera puede contactarnos. *


### Instalación de librerías

---

Para el correcto funcionamiento de esta herramienta se debe tener instalado en su máquina Python en su versión 3 además de las siguientes librerías:

* Notify
* Parser
* BeautifulSoup
* Requests

```python
pip install notify

pip install parser

pip install beautifulsoup

pip install request
```

### Conexión y Obtención de información

---

Para obtener los datos necesarios requerimos de pedirle los datos a la web y lo usaremos usando web scraping, para ello almacenamos la URL que se va a utilizar:

```python
html_crudo = "https://notify.moe/anime/fxRlqPDVR"
```

*[https://notify.moe/anime/fxRlqPDVR](https://notify.moe/anime/fxRlqPDVR)* es una web que nos proporciona un indexado de todos los animes que están en transmisión. Además de indicarnos que episodio ya han sido lanzado.

Luego de ello, pediremos una *requests* para obtener toda la información, de la misma manera guardamos toda la información en la variable *resultado* para luego obtener el *contenido* de la web a una forma que Python lo entienda con la ayuda de la función *.text* de la librería **Requests**.

```python
resultado = requests.get(html_crudo)
contenido = resultado.text
```

En este caso no necesitamos toda la web, solo cierta parte que nos interesa. Para ello pasamos ese contenido por nuestra librería **BeautifulSoup**, para saber más puedes ir a su [documentación](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) oficial.

```python
soup = BeautifulSoup(contenido, "html.parser")
```

Gracias a la librería BeautifulSoup podemos usar su función *find_all* que nos ayudara a encontrar y guardar en la variable *arreglo_elementos* todas las etiquetas `<a>` que contengan como clase (en HTML class="") la ID **data-mountable-type** y su valor **episode.** (Esto para hacer la búsqueda más concreta)

```python
arreglo_elementos = soup.find_all("a", {"data-mountable-type": "episode"})
```

Para el uso más cómodo de toda esta información requerimos que este en forma de STR. Para ello usamos una sencilla función.

```python
arreglo_str = [str(i) for i in arreglo_elementos]
```


### **Detección de episodios sin ser lanzados**

---

Para detectar cuales son los episodios que no han sido lanzados realizamos un ciclo buscando cada etiqueta `<a>` el estado *'data-available="false"'* esto con el fin de ir contando los episodios faltantes.

```python
contador = 0
string = 'data-available="false"'
for elemento in arreglo_str:
    if string in elemento:
        True
    else:
        contador += 1
```

Con el contador obtendremos el siguiente capitulo que se lanzara. Así que guardamos e insertamos ese número para solo obtener esa etiqueta `<a>` de ese episodio en concreto.

```python
nuevo_episodio = arreglo_str[contador]
```

Para luego nuevamente buscando el nuevo estado de *data-available="true"' .* Ya que nos ayudara para detectar que se ha lanzado el nuevo episodio y proceder a notificarlo.

Para ello realizamos una sentencia para saber si ese estado ha cambiado, si es así se lanzara una notificación. Esta notificación está hecha con la librería **Notify**.

```python-repl
cadena = 'data-available="true"'
if cadena in nuevo_episodio:
    notification = Notify()
    notification.title = "Anime"
    notification.message = "El anime esta actualmente."
    notification.send()
```


Expliquemos un poco el funcionamiento de la notificación. Para ello creamos una variable donde contendrán el método **Notify()**, ya con ello listo nos dará la posibilidad de usar varias funciones. La que vamos a usar son *.title* para el título de la notificación, *.message* para el mensaje en cuestión y ya por ultimo *.send()* para hacer efectivo la visualización.

## Aclaraciones

Por el momento solo se puede visualizar la notificación si se ejecuta el código en su IDLE de preferencia. Pero se está desarrollando para que sea una aplicación para la computadora y a futuro próximo una web.

#### Desarrolladores

azuzu0 - Head Project Developer

Danox - Second Head Project Developer
