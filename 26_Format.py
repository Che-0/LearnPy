#Nombre = input(str("Ingrese tu nombre: "))
#Edad = int(input("Ingrese tu edad: "))
#print("Tu nombre es {0} y tu edad {1} {0}".format(Nombre,Edad))
#
#resultdado: 
#Ingrese tu nombre: jose manuel
#Ingrese tu edad: 18
#Tu nombre es jose manuel y tu edad 18 jose manue

print("\nEjemplo 2\n")
a="abra" #0
b="cad"  #1
print("{0} {1} {0}".format(a,b))

#los identificadores tambien funcionan para alinear listas o datos 
print("{0:<5} {1:^20} {0:>10}".format(a,b))

# con el simbolo < se puede alinear a la izquierda
# con el simbolo ^ se puede alinear al centro
# con el simbolo > se puede alinear a la derecha
# el numero 10 es el numero de caracteres de espacio que se quiere que tenga el dato

#resultado:
# Ejemplo 2
#
#abra cad abra
#abra     cad           abra
