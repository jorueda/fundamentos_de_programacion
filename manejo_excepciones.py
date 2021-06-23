print("*** Manejo de excepciones en Python ***")

while True: # El while True solamente es para que vuelva a ejecutar, no tiene que ver con el try except.
    try:
        entrada = int(input("Ingrese un número entero: "))
        print("El valor ingresado es un entero.")
        break
    except ValueError:
        print("Error en los datos, debe ser un número entero.")
