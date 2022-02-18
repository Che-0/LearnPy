#while True:
#    try:
#        with open('18_Leer.txt', 'r+') as f:
#            contenido=f.read()
#            print(contenido)
#            break
#
#   except:
#        print('No se pudo abrir el archivo')
#        break

#lo de aca arriva es la confirmacion de que hay un error
#porque el archivo no existe

#programa en escencia 

#se creara una variable para guardar el archivo y despues el try 

dirarchivo='18_catos.txt'

while True:
    try:
        with open(dirarchivo, 'r+') as f:
            contenido=f.read()
            print(contenido)
            break
    except:
        print('No se pudo abrir el archivo')
        print("No se encontro el archivo", dirarchivo,"especifique dirrecion")
        dirarchivo=input("Ingrese la dirrecion del archivo: ")
        
