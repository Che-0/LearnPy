with open ("16_Archivos.txt","r") as f:
    contenido = f.read()
print(contenido)
#mostrara el contenido del archivo que creé en el 16 
#y lo mostrara en pantalla

#metodo readline()
#Lee una línea del archivo y devuelve una cadena con la línea leída.
#Si no hay más líneas, devuelve una cadena vacía.
#tu la especificas

with open ("16_Archivos.txt","r") as f:
    linea1=f.readline()  #<----leo la primera linea y la guardo en la variable linea1
    linea5=f.readline()  #<----leo la primera linea y la guardo en la variable linea1

print(linea1)
print(linea5)

#no es tan factible porque tengo que utilizar el metodo readline() por cada linea que quiera leer
#y eso es una operacion ineficiente

print("\n")
print("imprimiendo de linea 2 a linea 4\n")

with open ("16_Archivos.txt","r") as f:
    ramdom=(linea for i,linea in enumerate (f) if i>=2 and i<=5)
    for linea in ramdom:
        print(linea)

#la posicion la cuenta desde 0 we 

#metodo readlines()
print("\n") 
print("readlines()\n")

with open ("16_Archivos.txt","r") as f:
    texto=f.readlines()
    print(texto)

#metodo write()
print("\n")
print("metodo write()\n")

with open("16_Archivos.txt","r+") as f:
    cancion = f.read() #abrimos y almacenamos
    final_del_archivo=f.tell() #<----definimos var con el puntero al final del archivo
    f.write("\nThe strokes-Someday") #\n es para que se ponga un salto de linea
    f.seek(final_del_archivo) #<----definimos puntero al final del archivo
    contenido_editado=f.read()
    print(contenido_editado)

#metodo writelines()
print("\n")
print("metodo writelines()\n")

lista= ["\nCansion\n","sobre\n","estrellas"] #<----\n pa que salga debajo de the strokes

with open("16_Archivos.txt","r+") as f:
    rola = f.read() #abrimos y almacenamos
    finall_del_archivo=f.tell() #vamos a definir la posicion del puntero al final del archivo
    f.writelines(lista) #<----escribimos la lista en el archivo linea por linea
    f.seek(final_del_archivo) #<----nos trasladamos al final del archivo
    contenidoo_editado=f.read() #<----guardamos la nueva version del archivo
    print(contenidoo_editado) #<----imprimimos la nueva version del archivo