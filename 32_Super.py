#Esta funcion permmite invocar y conservar un metpo o atributo de la clase padre
#sin tenerlo que nombrar explicitamente 

#asi que nos brinda la ventaja de poder cambiar el nommbre de la clase padre o hija cuando queramos 
#y aun asi mantener un codigo funcional 

# Herencia somple de clases y atributos 
# ejemplo: queremos que una clase secundaria herede los atributos de la clase primaria
# #Si no recurrimos a la funcion de Super, o llamamos al metodo __init__ especificando los aatributos
# #Deberemos reescribirlos, lo cual seria una perdida de tiempo
# 

#class Padre ():     ----------ej
#    def __init__(self,ojos,cejas):  #atributosdel constructor de la clase padre
#        self.ojos=ojos
#        self.cejas=cejas

#class Hijo (Padre): ----------ej
#    def __init__ (self,ojos,cejas,cara): #Definimos los atributos en el constructor de la clase hija    
#        self.ojos = ojos #sobreescribimos los atributos
#        self.cejas = cejas
#       self.cara = cara     #nuevo atrivuto para la cria

#Tomas = Hijo ("verdees","cafes","redonda") #instanciamos
#print(Tomas.ojos,Tomas.cejas,Tomas.cara)
#resultado: verdees cafes redonda

#Tambien se podria hacer asi  -------------------------------------------

#class Padre (): -----------ej
  #  def __init__(self,ojos,cejas):  #atributosdel constructor de la clase padre
 #       self.ojos=ojos
 #       self.cejas=cejas

#class Hijo (Padre):
 #   def __init__ (self,ojos,cejas,cara):
  #      Padre.__init__(self,ojos,cejas) #especificamos la clase y llamamos a su constructor + atributos
 #       self.cara = cara     #nuevo atrivuto para la cria

#Tomas = Hijo("azules","cafes","redonda") #instanciamos
#print(Tomas.ojos,Tomas.cejas,Tomas.cara)
#resultado: verdees cafes redonda


#La forma utilizando la funcion super(), es casi el mismo codigo pero no necesitamos 
#especificar la clase padre. Por lo que podremos cambiarle el name si queremos 

#clas Padre ():----------------------------ej
#    def __init__(self,ojos,cejas):  #atributosdel constructor de la clase padre
#        self.ojos=ojos
#        self.cejas=cejas

#class Hijo (Padre):      ------------
#    def __init__ (self,ojos,cejas,cara):
#        super().__init__(ojos,cejas) #solicitamos a Super sa llamar de la clas padre a esos atributos  atributos
#        self.cara = cara     #nuevo atrivuto para la cria

#Tomas = Hijo('Marrones', 'Negras', 'Larga') ----------
#print (Tomas.ojos, Tomas.cejas, Tomas.cara)

#de esas dos formas llamamos al padre de la clase hojo para no perder si codigo
#y ademas agregamos un atrinuto nuevo 

#tambien podemos cambiar el nombre padre por cualquier otro y y la clase hijo heredera los atributos 
# de la clase padre

#No en super we, sino que Super como que identifica la clase a la quepertenece 


class Abuelo(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo(Abuelo): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara
        
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)
#El resultado sera el mismo 