#diccionario a partir de listas con bucle for

Lista= [ ("hola","compy"),("pi","to")] #aqui se crea una lista de tuplas [ (tupla1,tupla1),(tupla2,tupla2)]
print(Lista)

diccionario = {k:v for k,v in Lista} #creando un diccionario a partir de listas con bucle for
print(diccionario)