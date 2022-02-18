for x in range(1,11):
    print ('{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:1d}{3}'.format(x, x * x, x * x * x, '|'))
# el | es el caracter numero 3                             0    1         2      3     

#la letra d es para cuando son datos de tipo entero
#y la letra s es para cuando son datos de tipo string
# el 2d 3d y 4d son para como hacer espacios y darle formato
#asi se ve con el codigo actual
#| 1| |  1| |   1|
#| 2| |  4| |   8|
#| 3| |  9| |  27|
#| 4| | 16| |  64|
#| 5| | 25| | 125|
#| 6| | 36| | 216|
#| 7| | 49| | 343|
#| 8| | 64| | 512|
#| 9| | 81| | 729|
#|10| |100| |1000|

#pero si por ejemplo , cambio el 4 por 1 pasa esto
#| 1| |  1| |1|
#| 2| |  4| |8|
#| 3| |  9| |27|
#| 4| | 16| |64|
#| 5| | 25| |125|
#| 6| | 36| |216|
#| 7| | 49| |343|
#| 8| | 64| |512|
#| 9| | 81| |729|
#|10| |100| |1000|
#
#como que pierde el formato 
#digamos que el numero delimita el espacio que se quiere que tenga el dato
