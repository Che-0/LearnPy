#Los metodos de clase son similares a las variables de clase
# y nos permiten acceder a ellos sin instanciar un obje

class Animal(object):

	@classmethod

	def correr(self,km):
		print("El animal corrio %s kilometros" %km )  #format
		'clases para los animales corredores' #descripcion de esta clase

Animal.correr(12)

a = "pendejo"
b = "nah"

# Resultado 
#El animal corrio 12 kilometros

#como se puede apreciar no se necesita instanciar ningun objeto para hacer
# uso del metodo correr de la clase animal  , es muy importante el decorador 


