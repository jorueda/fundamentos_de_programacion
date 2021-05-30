"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1
#ejemplo1()

def actividad1():
    print("actividad1")
    numero = int(input("Ingrese un número: "))
    i = 2
    while i <= numero:
        print(i)
        i += 2
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

def actividad2():
    print("actividad2")
    numero = int(input("Ingrese un número: "))
    digitos = 0
    while numero > 0:
        numero = numero // 10
        digitos += 1
    print("El número tiene", digitos, "dígitos.")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

#actividad2()    
  

def actividad3():
    print("actividad3")
    contador = 0
    total = 0
    numero = float(input("Ingrese el número: "))
    while numero != -1:
        total += numero # es igual a: total = total + numero
        contador += 1 # es igual a: contador = contador +1
        numero = float(input("Ingrese el número: "))
    print("El promedio de todos los números es:", total/contador)
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).

#actividad3()

def actividad4():
    print("actividad4")
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    contador = exponente
    potencia = 1
    while contador != 0:
        potencia = potencia * base
        contador -= 1
    print("La potencia de", base, "a la", exponente, "es igual a =", potencia)

    # Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia.
    # No se puede utilizar el operador de potencia.

#actividad4()

def actividad5():
    print("actividad5")
    frase = input("Ingrese palabra o frase: ")
    pos_letra = 0
    contador = 0
    while pos_letra < len(frase):
        letra = frase[pos_letra].lower()
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            contador += 1
        pos_letra += 1
    print(f"El número de vocales en la palabra o frase es {contador}")
    # Realice un algoritmo en python que cuente cuantas vocales se encuentran dentro de una palabra o frase.

actividad5()