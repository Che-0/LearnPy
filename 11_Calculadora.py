#camara aqui empieza lo chido

def sumar():
    x = a + b
    print("el resultado es ",x)

def restar():
    x = a - b
    print("el resultado es",x)

def multiplicar():
    x = a * b
    print("el resultado es",x)

def dividir():
    x = a / b
    print(("el resultado es"),(x))

##############################################################
while True: #se crea el bucle 

    try:  #datos de la entrada

        a = int(input("Ingresa el primer numero: \n"))
        b = int(input("Ingresa el segundo numero: \n"))
        print("Qué calculo quieres realizar con",a,"y",b,"?\n")
        op = str(input("""
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        introdusca la opcion: """))

    except: #En caso de haber un error hacer 
        print("Error")
        #continue #se vuelve a ejecutar el bucle con esta wea de aqui pero lo hago comentario
        op="?"
    #si algo esta mal se termina la ejecucion 
##################################################################

    if op == "1":
        sumar()
        break
    elif op == "2":
        restar()
        break
    elif op == "3":
        multiplicar()
        break
    elif op == "4":
        dividir()
        break
    else:
        print("ha ingresado una pcion no valida")
        break
