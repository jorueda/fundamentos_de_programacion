"""
Cada ejemplo y actividad será definida como un bloque independiente.
Si-Sino-Finsi
Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 
El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

    Si (condición) Entonces
        instrucción(es)
    Sino Si
        instrucción(es)
    Fin Si

En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciónes. 
Por ejemplo:
"""
def ejemplo1():
    x = int(input("Por favor ingresa un número: "))
    if x < 0:
        print('El número es Negativo')
    elif x > 0:
        print('El número es positivo')
    elif x == 0:
        print('El número es cero')
# ejemplo1()

def actividad1():
    print("actividad1")
    semaforo = input("Ingrese el color del semáforo (Verde/Amarillo/Rojo): ").lower()
    if semaforo == "verde":
        print("Siga")
    elif semaforo == "amarillo":
        print("Precaución")
    elif semaforo == "rojo":
        print("Pare")
    else:
        print("El color escrito es incorrecto.")
        actividad1()
    #Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
# actividad1()

def actividad2():
    print("actividad2")
    semaforo = input("Ingrese el color del semáforo (Verde/Amarillo/Rojo): ").lower()
    if semaforo == "verde":
        hayPeaton = input("Hay peatón? (S/N) ").lower()
        if hayPeaton == "s":
            print("Pare.")
        else:
            print("Siga.")
    elif semaforo == "amarillo":
        hayPeaton = input("Hay peatón? (S/N) ").lower()
        if hayPeaton == "s":
            print("Pare.")
        else:
            print("Precaución")
    elif semaforo == "rojo":
        print("Pare")
    else:
        print("El color escrito es incorrecto.")
        actividad2()

#Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
#Verde -------- Si hay peaton - Pare, Sino - Siga
#Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
#Rojo = Pare

#actividad2()

def actividad3():
    print("actividad3")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print("1 para sumar a + b")
    print("2 para multiplicar a * b")
    print("3 para restar a - b")
    print("4 para dividir a / b")
    operacion = int(input("Ingrese la operación elegida: "))
    if operacion == 1:
        print("La suma a + b = ", a + b)
    elif operacion == 2:
        print("La multiplicación a * b = ", a * b)
    elif operacion == 3:
        print("La resta a - b = ", a - b)
    elif operacion == 4:
        if b == 0:
            print("La división por 0 no está permitida.")
            actividad3()
        else: print("La división a / b = ", a / b)
    else:
        print("Elija alguna operación matemática.")
        actividad3()
#Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 
#1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
#retornar el resultado de la operación indicada.

#actividad3()

def actividad4():
    print("actividad4")

    numero = input("Ingrese número de 4 dígitos: ")
    print(numero)
    if len(numero) == 4:
        print("Es un número de 4 dígitos.")
        digito1 = int(numero[0])
        digito2 = int(numero[1])
        digito3 = int(numero[2])
        digito4 = int(numero[3])
        maximo = max(digito1, digito2, digito3, digito4)
        print("El mayor dígito es:", maximo)
        if maximo % 2 == 0:
            print("Éste dígito es par.")
        else:
            print("Éste dígito es impar.")
    else:
        print("El número digitado no es de 4 dígitos.")

# Reto del día
# El objetivo de hoy es diseñar un programa con las siguientes opciones:
# 1.	Leer un número de 4 dígitos, mostrar el dígito mayor e informar si es par o impar.

#actividad4()

def actividad5():
    print("actividad5")

    numero1 = input("Ingrese primer número de 3 dígitos: ")
    numero2 = input("Ingrese segundo número de 3 dígitos: ")
    if len(numero1) == 3 and len(numero2) == 3:
        print("Ambos números son de 3 dígitos")
        digito11 = int(numero1[0])
        digito12 = int(numero1[1])
        digito13 = int(numero1[2])
        digito21 = int(numero2[0])
        digito22 = int(numero2[1])
        digito23 = int(numero2[2])
        mayor_primero = max(digito11, digito12, digito13)
        menor_segundo = min(digito21, digito22, digito23)
        numero3 = str(mayor_primero) + str(menor_segundo)
        print("El número resultante del mayor del primero y del menor del segundo es: ", numero3)
    elif len(numero1) != 3 and len(numero2) != 3:
        print("Ambos números no son de 3 dígitos.")
    elif len(numero1) != 3:
        print("El primer número no es de 3 dígitos.")
    else:
        print("El segundo número no es de 3 dígitos.")
        

# 2.	Leer dos números de 3 dígitos cada uno, formar un tercer número con el mayor del primero y el menor del segundo.

actividad5()