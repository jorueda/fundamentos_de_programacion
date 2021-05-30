# Ejercicio 2
# Juguemos al juego de adivinar el número, generaremos un número entre 1 y 100.Nuestro objetivo es adivinar el número. 
# Si fallamos nos dirán si es mayor o menor que el número buscado. 
# También poner el número de intentos requeridos.

import random
aleatorio = random.randint(1, 10)
adivinado = int(input("Ingrese un número del 1 al 10: "))
print(aleatorio)

if aleatorio == adivinado:
    print("¡Ganó!")
elif adivinado < aleatorio:
    print("El número ingresado es menor al que se va a adivinar")
elif adivinado > aleatorio:
    print("El número ingesado es mayor al que se va a adivinar")
else:
    print("Opción no válida.")