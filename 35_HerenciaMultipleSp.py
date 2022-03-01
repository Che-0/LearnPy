#En la herencia multimple de clase es donde se puede explotar Super 



class Perros():
	def ladrar(self):
		print("GUaaaaaaaaaaaaa   guaaaaaaaaaa")

	def grunir(self):
		print("Grrrrrrr GRRRRRRRRRRR")

class Cachine(perros):
	def ladrar(self):
		print("gua gua ")

	def grunir(self):
		print("ggggññññiii gñññii")

class pastor(self):
	def ladrar(self):
		print("gugu gugu taaa")

	def grunir(self):
		print("te estoy gueñendo")

class Shepadoodle (Cachine,pastor):
	def ladrar(self,veces):
		for cuantas in range(veces):
			super(Shepadoodle, self).ladrar()

Tommy = Pastor()
Piny = Caniche()
Cuchele = Shepadoodle()
Cuchele.ladrarx(5) # Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
                    #Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
                    #Imprimiria el ladrido del Pastor_Aleman
