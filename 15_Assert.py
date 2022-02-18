#se haec una comprovacion y en caso de ser falsa  se genera un error que podemos
#personalizar para detectar el fallo rapidamente.
#Una aserción es una comprobación de validez 
# (traducido al español como “afirmar”) que puedes prender
#  o apagar cuando hallas terminado de probar el programa.
#  Una expresión es probada y si el resultado es falso una excepción es levantada.

monedas = -19

if monedas >=12:
    print("tienes",monedas,"monedas, puedes comprar una pizza")

elif monedas <=12:
    print("tienes",monedas,"monedas, no puedes comprar una pizza")
    assert monedas >0,"error de comprobacion, monedas es negativo"
    