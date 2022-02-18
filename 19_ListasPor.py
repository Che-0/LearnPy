#para empezar, podria decir que hay dos tipos 
#de extension y de compresion

#extension tienes que declarar cada elemento uno por uno
#compresion no se declara un por uno, sino por un propiedad comun (tu especificas)

#extension
#a = [1,2,3,4]
#print(a)

#compresion
#a = [x for x in range(9) if x%2==0 ]
#print(a)
#resultado   [0,2,4,6,8]

#Podria decir que su estructura es 
# expresion   for     elemento    in     rango     if          condiciones etc

#Lista que estrae solo los nomnres cuya inicial sea vocal

vocales = ['A','E','I','O','U']

Nombres = ["Manuel","Ana","Ohtokamy","Akary","jose","L"]

NombresVocal = [nombre for nombre in Nombres if nombre[0] in vocales]
print(NombresVocal)

#la misma lista pero mejor 

print("\nlista num2\n")

NombresVocal = []

vocales = ['A','E','I','O','U']

Nombres = ["Manuel","Ana","Ohtokamy","Akary","jose","L"]

for nombre in Nombres: #Para el elemento nombre , iteramos la lista Nombres
    if nombre[0] in vocales: #Si eñ indice 0 del elemento nombre está en la lista vocales
        NombresVocal.append(nombre)#Agregamos el elemento nombre a la lista NombresVocal

print(NombresVocal)
#Este codigo esta mas chido  que el primero porque es mas netendible
#mas logico 
#en el ciclo for 