#En la herencia multimple de clase es donde se puede explotar Super 



class Perros(): #Clase padre
	def ladrar(self):
		print("GUaaaaaaaaaaaaa   guaaaaaaaaaa")

	def grunir(self):
		print("Grrrrrrr GRRRRRRRRRRR")

class cachine(Perros): #clase secundaria que hereda de la clase principal
	def ladrar(self):
		print("gua gua ")

	def grunir(self):
		print("ggggññññiii gñññii")

class pastor(Perros): #clase secundaria que hereda de la clase principal
	def ladrar(self):
		print("gugu gugu taaa")

	def grunir(self):
		print("te estoy gueñendo")

class Shepadoodle (pastor,cachine): #La clase hereda de las clases hijas de su padre Perros
	def ladrarx(self,veces):
		for cuantas in range(veces):
			super(Shepadoodle, self).ladrar() #esta estructura porque 2 clases entan dentro de ella
			                                   #por eso el self refiriendose a la que este primero 
Tommy = pastor()
#Tommy.grunir()
Piny = cachine()

Cuchele = Shepadoodle()
Cuchele.ladrarx(1) # Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
                    #Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
                    #Imprimiria el ladrido del Pastor_Aleman

#class Shepadoodle (cachine,pastor):
# cuando tiene esos argumento, a la hora de utilizar ladrarx va a poner el ladrido de cachine, que es el 1
#o sea gua gua

#pero si el argumento es class Shepadoodle (pastor, cachine):
#entonces el resultado sera el ladrido de pastor, que es gugu gugu taaa

#entonces esto tiene una gerarquia 
# si ponemos solo Perros, tomara el ladrido de la clase padre (Perros) el mas sivilizado
