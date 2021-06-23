# reto5.py

contador = 0
suma_acidez = 0
suma_materia = 0
minimo_acidez = 0
minimo_materia = 0
maximo_acidez = 0
maximo_materia = 0
no_apto = 0
marginalmente_apto = 0
moderadamente_apto = 0
sumamente_apto = 0

ciudad = input()

with open('data.csv', 'r') as archivo:
    temporal = []
    for fila in archivo:
        temporal = fila.rstrip('\n').split(",")
        if temporal[0] == ciudad:
            acidez = float(temporal[2])
            materia = float(temporal[3])
            if acidez > maximo_acidez:
                maximo_acidez = acidez
                if minimo_acidez == 0:
                    minimo_acidez = maximo_acidez
            elif acidez < minimo_acidez:
                minimo_acidez = acidez
            if materia > maximo_materia:
                maximo_materia = materia
                if minimo_materia == 0:
                    minimo_materia = maximo_materia
            elif materia < minimo_materia:
                minimo_materia = materia
            suma_acidez += acidez
            suma_materia += materia
            contador += 1
            if temporal[6] == "no apto":
                no_apto += 1
            elif temporal[6] == "marginalmente apto":
                marginalmente_apto += 1
            elif temporal[6] == "moderadamente apto":
                moderadamente_apto += 1
            elif temporal[6] == "sumamente apto":
                sumamente_apto += 1

print("{:.2f}".format(suma_acidez/contador) + " {:.2f}".format(suma_materia/contador))
print(minimo_acidez, minimo_materia)
print(maximo_acidez, maximo_materia)
print(f'no apto {no_apto}')
print(f'marginalmente apto {marginalmente_apto}')
print(f'moderadamente apto {moderadamente_apto}')
print(f'sumamente apto {sumamente_apto}')
