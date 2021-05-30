"""

Para

El ciclo Para o For en Python nos ayuda a ejecutar dentro dentro de un rango determinado de iteraciones. 
Esto es particularmente útil cuando usamos estructuras de datos que son inherentement "ordenadas"; listas, colecciones, cadenas de caracteres, etc.

En la semana uno exploramos el tipo de dato string (una cadena de caracteres). 
Los caracteres dentro de este tipo de dato en Python puede ser recorridos con la posicion en la que se encuentran dentro de la cadena. Veamos un ejemplo:
"""

import random

def ejemplo1():
    palabra = "Prueba"
    longitud = len(palabra)

    print("Primer ciclo")
    for i in range(longitud):
        print(palabra[i])

    print("Segundo ciclo")
    for x in "Prueba":
        print(x)

#ejemplo1()

"""
Vamos a modificar este ejemplo para conocer la longitud de la palabra y validar la ubicación de cada valor dentro de la cadena.
"""
def ejemplo2():
    palabra = "Prueba"
    longitud = len(palabra)

    print("Longitud", longitud)

    for i in range(longitud):
        print(i,palabra[i])

#ejemplo2()

def actividad1():
    print("actividad1")
    n = int(input("Ingrese cuántos números de la serie de Fibonacci: "))
    numero1 = 0
    numero2 = 1
    print(numero1, end=" ")
    for contador in range(n - 1):
        print(numero2, end=" ")
        suma = numero1 + numero2
        numero1 = numero2
        numero2 = suma

    # Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.
 
#actividad1()

def actividad2():
    print("actividad2")
    palabra = input("Ingrese una palabra: ")
    print(len(palabra))
    for contador in range(len(palabra)):
        print(palabra[contador])
        if palabra[contador] == "a":
            break

    #Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .

#actividad2()

def actividad3():
    print("actividad3")
    positivos = 0
    negativos = 0
    neutros = 0
    for numero in range(10):
        ingresado = random.randint(-10, 10)
        print(ingresado, end=" ")
        if ingresado > 0:
            positivos += 1
        elif ingresado < 0:
            negativos += 1
        else:
            neutros += 1

    print()
    print("Números positivos:", positivos)
    print("Números negativos:", negativos)
    print("Números neutros:", neutros)
    
    #Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).

#actividad3()

def actividad4():
    print("actividad4")
    numero = 0
    while numero != -1:
        numero = int(input("Ingrese un número para calcular el factorial, -1 para finalizar: "))
        if numero != -1:
            factorial = 1
            for contador in range (1, numero+1):
                factorial *= contador
                print(factorial, end=" ")
            print()
            print(f"El factorial de {numero} es {factorial}.")


    #Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de cada número ingresado usando un ciclo Para (For).
    
actividad4()