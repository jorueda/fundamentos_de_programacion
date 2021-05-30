# Diseñar 3 opciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
#   
# Luego crea un menú con las tres opciones.

def funcion1():
    #Escribe el código de la primera opción aquí
    numero = int(input("Digite un número de 4 dígitos: "))
    if len(str(numero)) != 4:
        print("El número no es de 4 dígitos")
    else:
        digito1 = (numero // 1000) % 10
        digito2 = (numero // 100) % 10
        digito3 = (numero // 10) % 10
        digito4 = numero % 10

        print("Los dígitos son: ", digito1, digito2, digito3, digito4)

        if digito1 > digito2 and digito1 > digito3 and digito1 > digito4:
            maximo = digito1
        elif digito2 > digito1 and digito2 > digito3 and digito2 > digito4:
            maximo = digito2
        elif digito3 > digito1 and digito3 > digito2 and digito3 > digito4:
            maximo = digito3
        else:
            maximo = digito4

        if maximo % 2 == 0:
            print("El mayor dígito es par.")
        else:
            print("El mayor dígito es impar.")
            
        print("El mayor dígito es: ", maximo) 

def funcion2():
    #Escribe el código de la segunda opción aquí
    numero1 = int(input("Digite un número de 3 dígitos: "))
    numero2 = int(input("Digite un número de 3 dígitos: "))
    if len(str(numero1)) != 3:
        print("El primer número no es de 3 dígitos.")
    elif len(str(numero2)) != 3:
        print("El segundo número no es de 3 dígitos.")
    else:
        digito11 = (numero1 // 100) % 10
        digito12 = (numero1 // 10) % 10
        digito13 = numero1 % 10
        digito21 = (numero2 // 100) % 10
        digito22 = (numero2 // 10) % 10
        digito23 = numero2 % 10
        if digito11 >= digito12 and digito11 >= digito13:
            mayor1 = digito11
        elif digito12 >= digito11 and digito12 >= digito13:
            mayor1 = digito12
        else:
            mayor1 = digito13
        if digito21 <= digito22 and digito21 <= digito23:
            menor2 = digito21
        elif digito22 <= digito21 and digito22 <= digito23:
            menor2 = digito22
        else:
            menor2 = digito23
        numero_final = mayor1 * 10 + menor2

    print(f"El nuevo número fusionado es: {numero_final}")

def funcion3():
    #Escribe el código de la tercera opción aquí
    numero = int(input("Ingrese un número de 3 dígitos: "))
    digito1 = (numero // 100) % 10
    digito2 = (numero // 10) % 10
    digito3 = numero % 10
    if digito1 >= digito2 and digito1 >= digito3:
        mayor = digito1
    elif digito2 >= digito1 and digito2 >= digito3:
        mayor = digito2
    else:
        mayor = digito3
    if digito1 <= digito2 and digito1 <= digito3:
        menor = digito1
    elif digito2 <= digito1 and digito2 <= digito3:
        menor =  digito2
    else:
        menor = digito3
    
    if digito1 != menor and digito1 != mayor:
        medio = digito1
    elif digito2 != menor and digito2 != mayor:
        medio = digito2
    else:
        medio = digito3

    print("El mayor número posible es: ", mayor, medio, menor)

def funcion4():
    #Escribe el código de la cuarta  opción aquí
    # Escriba un programa que pida un año y que escriba si es bisiesto o no.
    # Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí
    print("Año bisiesto")
    anno = int(input("Escriba un año: "))
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        print("El año", anno, "es bisiesto.")
    else:
        print("El año", anno, "no es bisiesto.")

def funcion5():
#     La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#     Los ingredientes para cada tipo de pizza aparecen a continuación.
#     Ingredientes vegetarianos: Pimentón -  Cebolla.
#     Ingredientes no vegetarianos: Peperoni – Jamón - Salmón.
#     Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
#     función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
#     Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
#     Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
#     que lleva.

    pizza = int(input("Elija si su pizza es vegetariana (1) o no vegetariana (2): "))
    if pizza == 1:
        vegetariana = int(input("Los ingredientes disponibles para la vegetariana son: Pimentón (1) o Cebolla (2): "))
        if vegetariana == 1:
            eleccion = "Pimentón"
        elif vegetariana == 2:
            eleccion = "Cebolla"
        print("La pizza vegetariana elegida es Mozzarela, Tomate y", eleccion)
    elif pizza == 2:
        no_vegetariana = int(input("Los ingredientes disponibles para la no vegetariana son: Peperoni (1), Jamón (2) o Salmón (3): "))
        if no_vegetariana == 1:
            eleccion = "Peperoni"
        elif no_vegetariana == 2:
            eleccion = "Jamón"
        elif no_vegetariana == 3:
            eleccion = "Salmón"
        print("La pizza no vegetariana elegida es Mozzarela, Tomate y", eleccion)
    else:
        print("No eligió ninguna pizza.")





if __name__ == "__main__":
    #Escribe el código aquí para que el usuario seleccione una opción. Llamas cada opción como
    #funcion1()
    #funcion2()
    #funcion3()
    #funcion4()

    opcion = input(" *** RETOS DE LA SESIÓN # 6 *** \n *** SELECCIONA UNA OPCIÓN DEL MENÚ *** \n 1. Informar si es par o impar \n 2. Formar un tercer número con el mayor del primero y el menor del segundo \n 3. Formar el mayor número posible con sus cifras \n 4. Año bisiesto \n 5. La pizzería \n")

    if opcion == "1":
        funcion1()
    elif opcion == "2":
        funcion2()
    elif opcion == "3":
        funcion3()
    elif opcion == "4":
        funcion4()
    elif opcion == "5":
        funcion5()
    else:
        print("¡Error! Función no válida.")