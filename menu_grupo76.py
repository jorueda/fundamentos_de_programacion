import os
import time
lista = []

def limpiar():
    os.system('clear')
    print("Tamaño de la lista:", len(lista))
    print(lista)

def agregar():
    elemento = input("Ingrese el elemento: ")
    lista.append(elemento)
    menu()

def mostrar():
    print(lista)
    time.sleep(3)
    menu()

def remover_elemento():
    elemento = input("Ingrese elemento a remover: ")
    while lista.count(elemento) > 0:
        lista.remove(elemento)
    else:
        print("El elemento no existe en la lista.")
    menu()

def remover_posicion():
    posicion = int(input("Ingrese la posición a remover de la lista: "))
    if posicion > 0 and posicion < len(lista):
        lista.pop(posicion)
    else:
        print("Esa posición no existe en la lista.")
        time.sleep(3)
    menu()

def longitud():
    print("Tamaño de la lista: ", len(lista))
    menu()

def ordenar_ascendente():
    lista.sort()
    print(lista)
    menu()

def ordenar_descendente():
    lista.sort(reverse = True)
    print(lista)
    menu()

def consultar_posicion():
    posicion = int(input("Ingrese la posición del elemento a consultar: "))
    print(f"En el índice {posicion} se encuentra la cadena {lista[posicion]}.")
    time.sleep(3)
    menu()

def menu():
    limpiar()
    menu = int(input("1. Agregar\n2. Mostrar\n3. Remover x nombre\n4. Remover x posición\n5. Tamaño lista\n6. Ordenar ascendente\n7. Ordenar descendente\n8. Consultar x posición\n9. Salir\nElija una opción: "))

    if menu == 1:
        agregar()
    elif menu == 2:
        mostrar()
    elif menu == 3:
        remover_elemento()
    elif menu == 4:
        remover_posicion()
    elif menu == 5:
        longitud()
    elif menu == 6:
        ordenar_ascendente()
    elif menu == 7:
        ordenar_descendente()
    elif menu == 8:
        consultar_posicion()
    else:
        print("Gracias por utilizar nuestro sistema.")

menu()