# Ejercicio 3
# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
# de tal forma que los primeros cinco minutos cuestan se cobran a 100 pesos por minuto, 
# los siguientes tres, 80 pesos, los siguientes dos minutos, 70 pesos, y a partir del décimo minuto, 50 pesos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde 10 %. 
# Realice un algoritmo para determinar cuánto debe pagar.

duracion_llamada = float(input("Duración llamada en minutos: "))

if duracion_llamada <= 5:
    costo = duracion_llamada * 100
elif duracion_llamada <=8:
    costo = 500 + ((duracion_llamada - 5) * 80)
elif duracion_llamada <=10:
    costo = 740 + ((duracion_llamada - 8) * 70)
else:
    costo = 880 + ((duracion_llamada - 10) * 50)

print(costo)

dia = input("¿Es domingo (S/N)")
dia = dia.lower()

if dia == "s":
    costo = costo * (1.03)
elif dia == "n":
    turno = input("Turno de la mañana o de la tarde (M/T) ")
    turno = turno.lower()
    if turno == "m":
        costo = costo * (1.15)
    elif turno == "t":
        costo = costo + (1.1)
    else:
        print("Se digitó incorrecto la jornada.")
else:
    print("Se digitó incorrecto si es domingo.")

print("Costo final de la llamada: ", costo)
