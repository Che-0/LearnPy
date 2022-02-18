#class Humano(): #Creamos la clase Humano
#    def __init__(self, edad, nombre, ocupacion): #Definimos el parámetro edad , nombre y ocupacion
#        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
#        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
#        self.ocupacion = ocupacion #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACION
#Persona1 = Humano(31, "Pedro", "Desocupado") #Instancia

#Para añadir un nuevo atributo a la clase solo se debe de añadir al metodo constructor
#y en el self
#si esta dentro del constructor es un atributo de instancia, por ello debe de especificarse un valor 
#a la hora de instanciar el objeto nuevo a partir de esta clase

#class Humano ():
#    def __init__(self, edad, nombre, ocupacion):
#        self.edad = edad
#        self.nombre = nombre
#        self.ocupacion = ocupacion
#persona1= Humano(31,"Talos","Militar")
#print(persona1.edad)  #resulta que asi sale solo un atibuto 


#self vendria a ser el objeto que se esta instanciando
# "este mismo objeto" o "si mismo"


#para añadir un nuevo metodo de instancia 
#existen tres pero solo estudiare uno de momentno 
#1. metodo de instancia   <----- Este es el que vere  
#2. metodo de clase
#3. metodo estatico

#metodo para retornar el valor de cada argumento(atributo) del objeto persona1

#para crear un nuevo metodo se debe de usr def y el nombre del metodo
#def (al igual que en las funciones o como la utilizamos para el metodo constructor)

#su sintaxis:
#def nombre_metodo(self, parametros):   <---no ponemos parametro en el codigo de abajo porque
#no lo sabemos aun

#parallamar al objeto:
#objeto.nombredelmetodo(parametros)

print("\nnuevo metodo\n")

class Humano ():
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

    #Creacion de un nuevo metodo 

    def presentar(self):
        presentacion=(f"Hola soy {self.nombre} y tengo {self.edad} años y soy {self.ocupacion}")
        print (presentacion)

persona1= Humano(31,"Talos","Militar")
persona2= Humano(19,"Manuel","Desocupado")
persona1.presentar()
persona2.presentar()

#en este caso dentro de los parametros del metodo incluimos SELF para hacer referencia al objeto instanciado
#aunque todaviano sepamos sunombre.


#para cambiar unatributo mediante un metodo:
#los metodos puedencambiar atributos de "ocupacion"

print("\nCambiar atributomediante metodo \n")

class Humano ():
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

    #Creacion de un nuevo metodo 

    def presentar(self):
        presentacion=(f"Hola soy {self.nombre} y tengo {self.edad} años y soy {self.ocupacion}")
        print (presentacion)

    def contratar (self, puesto):
        self.puesto = puesto
        print(f"{self.nombre} ha sido contratado como {puesto}")
        self.ocupacion= puesto


persona1= Humano(31,"Talos","Militar")
persona2= Humano(19,"Manuel","Desocupado")

persona1.presentar()
persona2.presentar()

persona1.contratar("jefe")
persona1.presentar()

#Lo más practico es crearmetodos para modificar los atributos de nuestro objeto
#siempre debden de crearse las variables de atributo comoprivadas y ser modificadas mediante metodos publicos 
#de esta forma se mantiene el principio de encapsulamiento