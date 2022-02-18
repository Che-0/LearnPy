#las except son errores generados en nuesrso programa, que no sean del programador
#si alguna funcion de nuestro programa genera un error, este se propaga  y genera que
#todo el programa se detenga

#manejar los errores evitara que nuestro programa deje de funcionar de golpe y nos dara
#la posibilidad de mostrar un mensaje de error personalizado al usuario en vez del 
#mensaje por defecto


# Try:          except:
#se puede traducir como un "intenta" , en el caso de producirse un error , este buscara 
#una especificacion para el en el bloque except

#En caso de generarse un error el programa seguira como normalmente

#calculadora        error de dividir entre 0


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

    try:  #En caso de error 

        a = int(input("Ingresa el primer numero: \n"))
        b = int(input("Ingresa el segundo numero: \n"))
        print("Qué calculo quieres realizar con",a,"y",b,"?\n")
        op = str(input("""
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        introdusca la opcion: """))

    
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

    #except: #En caso de haber un error hacer    #atrapa el error
            #Algo super importante es que el except general, es el que
            #se mostrara en cuallquier error no especificado 
            #sabiendo eso, el except de zero seria 

    except ZeroDivisionError:     #siempre va antes del general , cualquiera particular 
        print ("Nuestro calculador no permite dividir por cero, intenta otro calculo!")

    
    except:            #este es el general y siempre va al final
        print("Error")
        op="?"

        #continue #se vuelve a ejecutar el bucle con esta wea de aqui pero lo hago comentario
        #si algo esta mal se termina la ejecucion






#El error generado en la division por 0 es un error de tipo ZeroDivisionError
#El error generado en una variable no definida es un error de tipo NameError

#para solucionar eñ error de tipo ZeroDivisionError se usa el try except
#el Try ya abarca todo el while, entonces solo tenemos que agregar otro except 
#para el error de tipo ZeroDivisionError, y atraparlo ahí

#correccion arriba 
