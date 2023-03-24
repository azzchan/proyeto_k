## Changelog

v1.1.2a

* Se divide la logica del metodo `get_latest_espisode` ahora en vez de devolver el estado y el episodio, los hace en dos metodos independientes que son, `get_state_episode` y `get_Episode` respectivamente.
* Se mejora la logica del metodo `get_restTime`.
* Se agregaron varios metodos tales como:
  * `request` se encarga del manejo de las peticiones a la web.
  * `complete_link` se obtiene un link adecuado.
  * `get_Posicion` se encargara de obtener la posicion del anime en el vector.
  * `get_AnimeLink` obtencion del link que redireciona al anime, este es el complemento que requiere `complete_link` para funcionar.
  * `search_Anime` obtiene todo los posibles resultados de una busqueda. (Este metodo esta sujeto a cambios.)
