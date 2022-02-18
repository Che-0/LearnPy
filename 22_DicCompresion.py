#creando un diccionario por compresion 

dict((x,x*x) for x in range(5))

#para imprimirlo 

print(dict((x,x*x) for x in (1,2,3,4,)))

#Almacenarlo e imprimirlo

ss = (dict((x,x*x) for x in (1,2,3,4)))
print(ss)

#sintaxis
#dict(<clave>, <valor> for <elemento> in <iterable>)
