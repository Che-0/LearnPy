#Las listas son mutables y se pueden modificar
#pueden almacenar diferentes tipos de datos como strings, numeros, booleanos, etc   
#Las mismas se pueden editar y agregar elemento
#son como las estructuras de datos de C, pero sin tanto pedo 

#Estructura
# minitas = ["lau", "pau", "clau"]

#sintaxis

objetos = ["casa","coche","carro"] #son string, por eso las " "
numeros = [12,14,35,452,34,12] #son datos simples enteros

print(list(objetos))

#se puede acceder a los elementos de la lista con el indice [indice]

#El indice es el numero que se le asigna a cada elemento de la lista o tupla
#Este siempre comiena desde 0


#Slice       acceder a ellas en terminos simples 

numeros [0:2] #Accede a los elementos de la lista desde el indice 0 hasta el indice 2

print("Ejemplo de slice:\n")

print (numeros[0:6])  #numeros = [12,14,35,452,34,12] 
#aqui como que lo de empezaar desde el 0 vale verga
#porque el resulrado es [12,14,35] 3 posiciones

#si ponemos como parametro [:] nos muestra todo el arreglo
#si ponemos [:-2] nos muestra todo menos las dos ultimas posiciones
print (numeros[:-2])

#metodos (modificadores)
#append agrega un elemento al final de la lista (adjuntar)
#insert agrega un elemento en una posicion especifica
#pop elimina el ultimo elemento de la lista

#append (adjuntar)
print("\nEjemplo de append:\n")

list1 = ["gabriela","brisa","akary"]
print(list1)
list1.append("valeria")
print(list1)

#seagrego valeria al final de la lista
#list 1 = ["gabriela","brisa","akary","valeria"]

#extend
#Es casi lo mismo que append pero agrega a la lista letra por letra

print("\nEjemplo de extend:\n")
list1.extend(["manuel","jose","juan"])
print(list1)

#list 1 = ["gabriela","brisa","akary","valeria","manuel","jose","juan"]

#si llegara a poner list1. apend(jose) lo que va apasar es que va a agregar 
# ["gabriela","brisa","akary","valeria","manuel","j","o","s","e"] tomando cada letra
#como un parametro

list2 = [ 1,2,3]
list3 = [4,5,6]

list2.extend(list3) #list2 = list2 + list3 <- funciona igual
print("\anexar listas:\n")
print(list2)

#insert
#estructura
#lista.insert(posicion,elemento a agragar)

lista4 = ["flor","dulce","rosa"]

print("\nEjemplo de insert:\n")

lista4.insert(2,"amarillo")
print(lista4)

#metodo pop para eliminar elementos
#su estructura es lista.pop(posicion) , sidejas vacia la posicion se elimina el ultimo elemento

print("\nEjemplo de pop:\n")

lista4.pop(3)
print(lista4)

#remove

print("\nEjemplo de remove:\n")

lista4.remove("flor")
print(lista4)