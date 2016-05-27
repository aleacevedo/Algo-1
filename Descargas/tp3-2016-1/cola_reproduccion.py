import os
import ListaEnlazada

from cancion import Cancion

EXTENSIONES_ACEPTADAS = ("wav", "mp3", "flac", "ogg", "wma")

class ColaDeReproduccion:
	"""Clase que representa la cola de reproduccion del reproductor. Permite agregar y remover
	canciones, ademas de poder hacer y deshacer estas acciones. Las canciones se guardan en la
	cola como objetos de clase Cancion."""

	def __init__(self, lista_canciones = []):
		""" Recibe una lista de objetos de clase Cancion con las canciones que se quieren
		reproducir."""
		self.lista=ListaEnlazada.ListaEnlazada()
		self.prim=None
		self.actual=self.prim
		for x in lista_canciones:
			agregar_cancion(x.ruta)
		#raise NotImplementedError()

	def cancion_actual(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion actual, o None si no
		hay canciones cargadas en la cola."""
		return self.actual
		#raise NotImplementedError()

	def cancion_siguiente(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion siguiente en la cola,
		o None si no hay mas canciones."""
		self.actual=self.actual.prox
		return self.prim.prox
		#raise NotImplementedError()

	def cancion_anterior(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion anterior en la cola,
		o None si no hay canciones en la misma o la actual es la primera de la cola."""
		self.actual=self.atenrior
		return self.actual
		#raise NotImplementedError()

	def agregar_cancion(self, ruta_cancion):
		""" Agrega una Cancion a la cola a partir de su ruta. Devuelve True si se agrego
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		if(self.prim==None):
			#Usar tinytag y compleatar parametros
			self.prim=Cancion(ruta_cancion)
			self.prim.anterior=None
			self.actual=self.prim
			self.lista.append(["add",self.prim])
		else:
			actual=self.prim
			while actual.prox is not None:
				actual=actual.prox
			actual.prox=Cancion(ruta_cancion)
			actual.prox.atenrior=actual
			self.lista.append(["add",actual.prox])
		#raise NotImplementedError()

	def remover_cancion(self, ruta_cancion):
		""" Remueve una Cancion de la cola a partir de su ruta. Devuelve True si se removio
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		anterior=self.prim
		actual=anterior.prox
		if(anterior.ruta is ruta_cancion):
			self.lista.append(["rm",anterior])
			self.prim=anterior.prox
			return True
		else:
			try:
				while(actual.ruta is not ruta_cancion):
					anterior=actual
					actual=actual.prox
				self.lista.append(["rm",actual])
				anterior.prox=actual.prox
				return True
			except AttributeError:
				return False

		#raise NotImplementedError()

	def deshacer_modificacion(self):
		""" Deshace la ultima accion realizada. Devuelve True si pudo deshacerse, False en caso
		contrario."""
		try:
			hecho=self.lista.pop()
			if(hecho[0] is "rm"):
				self.agregar_cancion(hecho[1].ruta)
				return True
			elif(hecho[0] is "add"):
				self.remover_cancion(hecho[1].ruta)
				actual=self.prim
				return True
		except IndexError:
			return False
		raise NotImplementedError()

	def rehacer_modificacion(self):
		""" Rehace la ultima accion que se deshizo. Devuelve True si pudo rehacerse, False en caso
		contrario."""
		raise NotImplementedError()

	def obtener_n_siguientes(self, n_canciones):
		""" Devuelve una lista con las siguientes n canciones. Si en la cola de reproduccion
		quedan menos canciones que las pedidas, la lista contendra menos elementos que los
		pedidos."""
		raise NotImplementedError()
