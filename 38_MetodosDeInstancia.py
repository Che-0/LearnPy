class Ave (object):
	'clase para las aves'
	def __init__(self):
		pass #le indica al program que ignore esa condicion y sigue de continuo

	def hablar (self, color):
		print("Soy una jodida ave de clor %s" %color)

#Ave.hablar ('verde') #-> No puedes acceder de esta manera porque es un método de instancia

#debemos instanciar instanciar 

Loro = Ave()
Loro.hablar('verde') #invocamos el metod instancia

