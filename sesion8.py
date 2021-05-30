import random

"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

La opción break, puede parar el ciclo aunque la condición sea real. Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1 
#ejemplo1()

def actividad1():
    print("actividad1")
    numero = int(input("Ingrese un número: "))
    contador = 2
    while (contador <= numero):
        print(contador)
        if contador == 10:
            break # Termina el ciclo while
        contador += 2
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()


"""
La opción continue, puede continuar el ciclo y saltarse cuando sea verdadera. Por ejemplo:
"""
def ejemplo2():
    i = 1
    while i < 6:
        if i == 3:
            i += 1 
            continue # Vuelve hacia el while
        print(i)
        i += 1 

#ejemplo2()

def actividad2():
    print("actividad2")
    numero = int(input("Ingrese un número para contar: "))
    cadena =  str(numero)
    contador = 0
    total = 0
    longitud = len(cadena)
    while contador < longitud:
        if cadena[contador] == "4":
            contador += 1
            continue
        contador += 1
        total += 1
    print("El número ingresado fue:" ,numero)
    print("El número de digitos sin el 4 es:", total)
    # Escribe el código un ciclo para obtener el número de dígitos de un número 
    # ingresado por el usuario pero saltarse si el digito es 4.

#actividad2()

def ejercicio1():

    secreto = random.randint(1, 100)
    print(secreto)
    numero = int(input("Ingrese un número: "))
    intentos = 1
    while numero != secreto:
        if numero > secreto:
            print("El número ingresado es mayor al secreto.")
        else:
            print("El número ingresado es menor al secreto.")
        numero = int(input("Ingrese un número: "))
        intentos += 1
    print(f"Encontraste el número en {intentos} intentos.")

    # Ejercicio propuesto 1
    # Escribir un programa en python que obtenga un número aleatorio 1-100 secreto, y luego 
    # permita al usuario ingresar números y le indique sin son menores o mayores que el 
    # número a adivinar, hasta que el usuario ingrese el número correcto.
    # guarde el número de intentos utilizados.

#ejercicio1()

def ejercicio1_1():

    secreto = random.randint(1, 100)
    print(secreto)
    numero = int(input("Ingrese un número: "))
    intentos = 1
    while (True): # El mismo ejerciio anterior pero utilizando While (True)
        if numero > secreto:
            print("El número ingresado es mayor al secreto.")
        elif numero < secreto:
            print("El número ingresado es menor al secreto.")
        else:
            print(f"Encontraste el número en {intentos} intentos.")
            break # El mismo ejerciio anterior pero utilizando break
        numero = int(input("Ingrese un número: "))
        intentos += 1
    
#ejercicio1_1()

def ejercicio2():

    persona1 = int(input("Ingrese el km de la persona 1: "))
    persona2 = int(input("Ingrese el km de la persona 2: "))

    while persona1 != persona2:
        if persona1 < persona2:
            persona1 += 10
            persona2 -= 10
        else:
            persona1 -= 10
            persona2 += 10
    
    print("Ambas personas se encontraron en:", persona1)

    # Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra 
    # en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. 
    # Realizar un programa para determinar en qué kilómetro de esa carretera se 
    # encontrarán.

ejercicio2()