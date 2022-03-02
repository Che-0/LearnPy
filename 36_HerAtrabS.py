#Herencia multiple y atributos con super

# super() no nos sirve en ese caso. Debemos llamar a los constructores de ambas 
# clases especificandolas por su nombre. Y si cambiamos el nombre u orden de la clase
#  deberemos especificarlo!

class Padre(object):
    def __init__(self,ojos,cejas):
        self.ojos = ojos
        self.cejas = cejas

class Madre(object):
    def __init__(self,brazos,piernas):
        self.brazos = brazos
        self.piernas = piernas

class Hijo(Padre,Madre):
    def __init__(self,ojos,cejas,brazos,piernas,cara):
        Padre.__init__(self,ojos,cejas)
        Madre.__init__(self,brazos,piernas) #Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara

Tomas = Hijo("azules","cafes","largos","cortas","redonda")
print(Tomas.ojos,Tomas.cejas,Tomas.brazos,Tomas.piernas,Tomas.cara)