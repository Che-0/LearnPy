#llamar un metodo de otra clase padre con super()

class agregarelementos (list): #creamos una clase agregarelementos heredando atributos y metodos de la clase list
    def append (self,alumno):
        print (("Añadimos alumno" ), (alumno))
        super().append(alumno)

Lista1 = agregarelementos()
Lista1.append("Juan")
Lista1.append("Pedro")
print (Lista1)
