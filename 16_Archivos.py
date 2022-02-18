#Objeto file
#Crear un archivo llamado 16_Archivos.py

#estructura
# variable + open +ruta + modo de abrir
#"la var toma como valor el archivo y se convierte en un objeto"}


#f = open("16_Archivos.txt","w")
#f.write("Creando un archivo con python")
#f.close()

#--------------------Utilizando whit as---------------------------
with open ("16_Archivos.txt","w") as f:
    f.write("Creando un archivo con python")
    f.close()

#la w es re importante, porque es write
#se puede traducir como 
#abrir "16_Archivos.txt" en modo "w" como f

#--------------------Utilizando whit as explicacion cabrona ---------------------------
#with open ("Nombre", "modo de apertura") as Objeto:
 #    Objeto.Write() #<----Método escribir del objeto 


#Recordar que las líneas debajo de with as deben ir identadas!
