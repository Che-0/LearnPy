#cuando una clase secundaria hereda atributos y metodos de mas de una clase principal
#sintaxis
#class NombredeClase(Clase1,Clase2,Clase3):   solo basta con separar por comas

class Estudiante(object):
    def __init__(self,edad,nombre):  #la clase con el metodo constructor es la PADRE
        self.edad=edad
        self.nombre=nombre

class Instituto(object):
    def presentarinstituto(self): #metodo
        print("Estudio en la FES ARG")

class Derecho (Estudiante,Instituto):
    def presentarse (self):    #metodo
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")
        

Manuel = Derecho (19,"Manuel")
Manuel.presentarse()
Manuel.presentarinstituto()