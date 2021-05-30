"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
En Python, definimos una función con la siguiente estructura

def funcion(parametros)

Recuerda que los parametros son opcionales!
"""

def suma(a,b):
    
    print(a+b)

#suma(3,4)


#Actividad 1

def imprimaProducto(nombre, precio):
    print(f"{nombre} ${precio}")

def caja():
    valor_total = 0
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        valor_total += precio
        imprimaProducto(nombre, precio)
        print(f"Subtotal ${valor_total}")
        pregunta = input("Digite cualquier tecla para continuar, -1 para terminar: ")
        if pregunta == "-1":
            print(f"El valor total de la compra es ${valor_total}")
            break


#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar

#caja()

#Actividad 2

def numAleatorio():
    import random
    while True:
        aleatorio = random.randint(100, 130)
        if aleatorio == 110 or aleatorio == 115 or aleatorio == 120:
            continue
        else:
            return aleatorio

def numeros():
    for contador in range(10):
        while True:
            numero = numAleatorio()
            if contador % 2 == 0 and numero % 2 == 0:
                print(f"{contador + 1} {numero} Par")
                break
            elif contador % 2 != 0 and numero % 2 != 0:
                print(f"{contador + 1} {numero} Impar")
                break
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.

numeros()
