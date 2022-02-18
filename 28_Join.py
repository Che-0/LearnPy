#join nos permite convertir listas / tuplas en cadenas de texto y viceversa
#las listas son mutables, las cadenas no 

ListasAlumnos = [['Juan', 'Carmelo', 5, 7, 9, 7], ['Laura', 'Jazmine', 7, 8, 5, 6.66],
['Dario', 'Villalobos', 5, 6, 3, 4.66], ['Marito', 'Tasolo', 4, 7, 9, 6.666],
['Esteban', 'Quito', 9, 9, 8, 8.66]]

Tabla ="""\
+--------------------------------------------------------------------+
| Nombre    Apellido    primero     segundo     tercero     promedio |
|--------------------------------------------------------------------|
{}
+--------------------------------------------------------------------+\
"""
#                                  namecomplet |calificaciones   | promedio
Tabla = (Tabla.format('\n'.join("| {:<8} {:<10} {:>8} {:>6} {:>7} {:>22} |".format(*fila)
for fila in ListasAlumnos)))
#no le ponemos el numero de la variable porque con for estamos iterando desde la posicion 0

print(Tabla)
