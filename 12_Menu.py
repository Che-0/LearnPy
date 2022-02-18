#jugando con el bucle infinito de while True

while True:
    opcion = input("""Elige una fruta para tu desayuno:
    1. Pera
    2. Manzana
    3. Naranja
    4. Limon
    5. nada  
    """)

    if opcion == "1":
        print("Usted ha escogido la pera")
        break
    elif opcion == "2":
        print("Usted ha escogido la manzana")
        continue
    elif opcion == "3":
      #  print("Usted ha escogido la naranja")
        pass
        break
    elif opcion == "4":
        print("Usted ha escogido el limon")
        break
    elif opcion == "5":
        print("Usted no ha escogido nada")
        break
    else:
        print("Ha ingresado una opcion no valida, debes de seleccionar una de las opciones")
      #  break no ponemos el break para que el we seleccione una opcion valida 

print("Fin del programa, que disfrutes tu desayuno")

#para controlar los bucles se encuentran tres formas
# la primera es el break, que detiene el bucle

# la segunda es el continue, que te reiniara el bucle, te devuelve al inicio en pocas palabras
# si lo pusiera en la opcion 2, el programa se reiniciaaría , ahi la woa dejar

#la tercera es pass, su funcion es nula, como si no existiera
#pero nos permite crear un bucle sin colocar codigo en su cuerpo para añadirlo mas tarde 
#es un relleno temporal, el ejemplo esta en el 3 