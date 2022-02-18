Numeros = []

while True:
    Numerito1 = int(input("Ingrea un numero mayor de 5 y menor de 10:"))
    Numeros.append(Numerito1)
    Numerito2 = int(input("Ingrea un numero mayor de 5 y menor de 10:"))
    Numeros.append(Numerito2)
    Numerito3 = int(input("Ingrea un numero mayor de 5 y menor de 10:"))
    Numeros.append(Numerito3)
    print(Numeros)

    if all (numero>=5 and numero<=10 for numero in Numeros):
        print("Todos los numeros estan en el rango")
        print("Fin del programa")
        break
    elif any (numero>=5 and numero<=10 for numero in Numeros):
        print("Alguno de los numeros no esta en el rango")
        Numeros=[]   #reseteamos la lista
        print("Vuelve a intentarlo")
    
    else:
        print("Ninguno de los numeros esta en el rango")
        print("Nah mame, ni un pinche numero bien")
        break
