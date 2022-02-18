#Los diccionarios son mutables y vendrian siendo estructuras de datos
#lo mas importante, en estos se almacenan claves y valores keys and values
#los diccionarios se crean con {}

#sintaxis

#uwu = {
# 'key':'value'
# }

#se puede poner todo junto pero se ve feo
#cuando ya no se va a agregar otro k y v se deja de poner ","

mi_diccionario = {

"Nombre" : "Manuel",
"Edad" : 19,
"Genero" : "Masculino"

}

#Acceder al diccionario

Brisa = {
    "Nombre" : "Brisa",
    "Edad" : 19,
    "Genero" : "Femenino",
    "Alias" : "La artista",
    "Dulces favoritos" :[ "Chocolate", "panditas"], #lista
    "Estado civil" : "Casada",
    "hijos" : 3,
    "Hobbies" : ["Dibujar", "Leer", "pistear de vez en cuando"],#lista
    "Mascota" : "Gato",
    "ropa favorita" : "'holgada de preferencia'"
}

#imprimir el valor de una clave 
print (Brisa["Nombre"])

#para acceder a una lista dentro de un diccionario

#[posicion]
#[inicio:final]

print(Brisa["Dulces favoritos"][1])

#modificar datos del diccionario

#agrea una clave y valor
#key  "ingresos de sus pinturas" :  value : 100000

#las claves son unicas, asi que si ya existe, solo cammbia el valor

#sintaxis
#[key] = value

Brisa["Ingresos de sus pinturas"] = 10000

print(Brisa)

#modificar una lista dentro de un diccionario     modificar valor de una lista

#se aplica lo que dije antes, si ya existe, pues ....

Brisa["Ingresos de sus pinturas"] = 2000000
print(Brisa)

#modificar clave de una lista 
#metodo pop()          eliminar

Brisa["Sueldo"] = Brisa.pop("Ingresos de sus pinturas")
print(Brisa)

#se pone la clave nueva que quieres y despues la que tiene para eliminarla y
#sustituirla por la nueva con pop

#Para eliminar un par de key and value 
#del [key]

del(Brisa["hijos"])
print(Brisa)

Brisa["Esposo"] = "Chayanne"

print(Brisa.get("Esposo", "No tiene esposo"))

#metodo Get
#nos sirve para obtener el valor determinad de una clave o valor }

print(Brisa.get("ropa favorita", "No tiene ropa favorita"))
print(Brisa.keys())
print(Brisa.values())