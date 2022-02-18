#programa que separa nombres masculinos y femeninos dependiendo de a y e 

#el no optimizado 

#Listasfemeninos = []
#ListasMasculinos = []

#Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
#'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

#for nombre in Nombres:
#   if nombre[-1]=="a" or nombre[-1]=="e":
#        Listasfemeninos.append(nombre)
#    else:
#        ListasMasculinos.append(nombre)

#print(Listasfemeninos)
#print("-----------------")
#print(ListasMasculinos)
#
#el optimizado
print("\noptimizacion\n")

Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

Listasfemeninos =[nombre for nombre in Nombres if nombre[-1] =="a" or nombre[-1] =="e"]
ListasMasculinos =[nombre for nombre in Nombres if nombre[-1] !="a" and nombre[-1] !="e"]
print(Listasfemeninos)
print("-----------------")
print(ListasMasculinos)