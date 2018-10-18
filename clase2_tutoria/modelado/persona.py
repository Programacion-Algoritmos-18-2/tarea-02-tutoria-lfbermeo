class Persona:
	def __init__(self):
		self.nombre=""
		self.edad=0

	def agregar_nombre(self,n):
		self.nombre=n

	def obtener_nombre(self):
		return self.nombre

	def agregar_edad(self,e):
		self.edad=e

	def obtener_edad(self):
		return self.edad	

	def presentar_datos(self):
		cadena ="%s-%d"%(self.nombre, self.edad)
		(self.obtener_nombre(),self.obtener_edad())

		return cadena