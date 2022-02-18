#Herencia simple
#Cuando una clase hija hereda los atributos y metodos de una unica clase padre

class Estudiante(object):
    def __init__(self,edad,nombre):  #la clase con el metodo constructor es la PADRE
        self.edad=edad
        self.nombre=nombre

class Derecho(Estudiante):     #Clase secundaria con la clase principal dentro de 
    def presentarse (self):    #metodo
        print(f"Hola soy {self.nombre} y tengo {self.edad} años") 

Manuel = Derecho (19,"Manuel")
Manuel.presentarse()

#Derecho hereda los atributos de estudiante 

#declarar una clase principal

#class NombredeClase(object):
#    def __init__(self,atributo1,atributo2):
#        self.atributo1=atributo1             <----declaracion del atributo (objeto)

#si queremos que una clase herede de otra clase, debemos declararla como una clase secundaria
#class NombredeClase(NombredeClasePadre):

