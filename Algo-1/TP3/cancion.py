from tinytag import TinyTag

class Cancion:
	""" Objeto que almacena informacion de una cancion: su ruta, titulo y artista.
	Obtiene la informacion a partir de los tags del archivo, si los tiene."""

	def __init__(self, ruta, titulo = "Cancion desconocida", artista = "Autor desconocido"):
		# Usar TinyTag para obtener la informacion de la cancion, sobreescribir con lo pasado por
		# parametro solo si la informacion no se encuentra disponible
		self.ruta=ruta
		tag = TinyTag.get(ruta)
		self.titulo=tag.title if tag.title is not None else titulo
		self.artista = tag.artist if tag.artist is not None else artista
		self.prox=None
		self.anterior=None
		#raise NotImplementedError()

	def obtener_ruta(self):
		""" Devuelve la ruta del archivo de la cancion."""
		return self.ruta
		#raise NotImplementedError()

	def obtener_titulo(self):
		""" Devuelve el titulo de la cancion."""
		return self.titulo
		#raise NotImplementedError()

	def obtener_artista(self):
		""" Devuelve el artista de la cancion."""
		return self.artista
		#raise NotImplementedError()
