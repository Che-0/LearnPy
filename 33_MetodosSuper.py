#llamar un metodo de otra clase padre con super()

class agregarelementos (list): #creamos una clase agregarelementos heredando atributos y metodos de la clase list
    
    def append (self,alumno): #Creamoes el metodo append que añadira el elemento alumno 
        print (("Añadimos alumno" ), (alumno))
        super().append(alumno) #Incorporamos la funccion Super IN INDICAR LA CLASE ACTUAL, seguida de metodo append alm

Lista1 = agregarelementos() #Definimos la clase de nuestra lista llamada Lista1
Lista1.append("Juan")
Lista1.append("Pedro") #llamamos al metodo append de Lista1 con el argumento Pedro 
print (Lista1) #imprimimos la lista 

