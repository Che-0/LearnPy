#Sintaxis
#En el caso de un bucle for, se debe de especificar la variable donde
#se alojan los items del elemento iterable

#se coloca la sentencia for seguida de la variable donde se alojan los items y luego 
#del operador in el elemento a iterar

##for variable in elemento_iterable:
    #codigo a ejecutar

#ejemplo    extraer pares

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for par in numeros:  #par almacena los items de la lista 
    if par % 2 == 0:
        print(par)

for par in numeros:
    if par % 2 != 0:
        print(par)
#aqui estamos creando un bucle que itera sobre la lista numeros 
#almacenado los items en la variable par e imprimiendo aquellos que cumplan la condicion
#si quisieramos imprimir solo los impares seria !=0

print("\nUsos en listas\n")

palabras = ["hola", "mundo", "como", "estas", "todo", "bien"]

for caracteres in palabras:
    print(caracteres,"su longitud es:", len(caracteres))

print("\nUsos en diccionarios\n")
agenda = {
    "Nombre" : "Manuel",
    "Edad" : 19,
    "Genero" : "Masculino",
    "Numero" : "123456789"
}

for (key,value) in agenda.items():
    print(key,":",value)


#ejemplo de bucle for strings
print("\nUsos en strings\n")

texto = "Hola mundo vete a la vergaa we"
contador = 0
cuentalaletra = "a"

for letra in texto:
    if letra == cuentalaletra:
        contador += 1
print(cuentalaletra,"aparece ",contador,"veces")