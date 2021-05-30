"""
Vectores/Listas

Como vimos en la parte teórica, los vectores son una estructura de dato organizada que nos permite 
almacenar información. Una de las implementaciones más utilizadas es Python son las listas (List). 

Nota: En Python hay algunas diferencias menores entre un arreglo (array) y una lista, 
pero por ahora vamos a asumir que son lo mismo.

Vamos a ver una definición de esta estructura en Python. Para crear una lista, utilizamos los corchetes 
y separamos los valores de nuestra estructura con una coma. 

Por ejemplo, en la siguiente instrucción estamos creando una lista llamada a con los valores 1, 3, 2, 5, 2.
"""

def ejemplo1():
    a = [1, 3, 2, 5, 2]
    print(a)

#ejemplo1()

#Las listas no necesariamente tienen que ser de números, también pueden ser de texto:
def ejemplo2():
    nombres = ["María", "Juan","Andrés"]
    print(nombres)

#ejemplo2()

#Aquí van algunas funciones útiles cuando trabajamos con listas.
#    append(x) - inserta un nuevo valor x al final de la lista
#    remove(x) - remueve el primer valor X de la lista
#    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
#    len(x) - permite calcular el tamaño de una lista
#
# Ahora, veamoslas en acción
def ejemplo3():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))
#ejemplo3()

#Actividad 1
def actividad1():

    def obtener_lista(cantidad):
        lista = []
        indice = 0
        for contador in range(1, cantidad + 1):
            if contador % 2 == 0:
                lista.append(contador)
        return lista

    def imprimir_lista(lista):
        for contador in lista:
            print(contador)

    lista_pares = obtener_lista(10)
    imprimir_lista(lista_pares)

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los numeros pares del 1 al 10 
# y usa un ciclo para que los imprima

#actividad1()

#Actividad 2
def actividad2():
    import random

    longitud_lista = 6

    def aleatorios(): # Genera numero aleatorios sin repetir hasta la longitud_lista
        lista = []
        contador = 0
        while contador < longitud_lista:
            numero_generado = random.randint(1, 20)
            if lista.count(numero_generado) > 0:
                continue
            else:
                lista.append(numero_generado)
                contador += 1

        return lista

    def mayor(listado):
        mayor = max(listado)
        print(f"El número mayor es: {mayor}")

    def primos(listado):
        for numero in listado:
            for contador in range(2, numero):
                if numero % contador == 0:
                    break
            else:
                print(f"{numero} es un número primo.")


    listado = aleatorios()
    print(listado)
    mayor(listado)
    primos(listado)

#
#Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y 
#creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos

actividad2()