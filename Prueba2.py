import random
from random import randrange
from time import sleep


def crearbaraja(lista):
    i = 0
    cuenta = 1
    for i in range(52):
        lista[i] = cuenta
        cuenta = cuenta + 1
        if cuenta == 14:
            cuenta = 1


def mezclarbaraja(lista):
    for i in range(199):
        pos_azar1 = randrange(52)
        pos_azar2 = randrange(52)
        while pos_azar1 == pos_azar2:
            pos_azar2 = randrange(52)
    memoria = lista[pos_azar2]
    lista[pos_azar2] = lista[pos_azar1]
    lista[pos_azar1] = memoria


# Tomar carta
def tomarcarta(lista, posicion):
    resultado = lista[posicion]
    if resultado > 10:
        resultado = 10
    elif resultado == 1:
        print("sacaste un AS, cuanto debe valer 1 o 10?")
        resultado = int(input())
        while resultado != 1 and resultado != 10:
            print("valor no valido, reingrese")
            resultado = int(input())

    posicion += posicion + 1
    return resultado


# Tirada del jugador
def tiradajugador(lista, posicion, puntuacion):
    plantado = False
    while puntuacion < 22 and plantado == False:
        puntuacion += puntuacion + tomarcarta(lista, posicion)
        print("tu puntuacion es ", puntuacion)
        if puntuacion < 22:
            print("Te plantas S/N?")
            respuesta = str(input())
            while respuesta != "S" and respuesta != "N":
                print("Escribiste mal, Te plantas S/N?")
                respuesta = str(input())
            if respuesta == "S":
                plantado = True
            else:
                plantado = False
    if puntuacion > 21:
        print("Perdiste!")
    else:
        print("Turno Crupier")


# Tomar carta Crupier
def tomarcartacrupier(lista, posicion, puntosjugador, puntoscrupier):
    resultado = lista[posicion]
    if resultado > 10:
        resultado = 10
    if resultado == 1:
        print("es un As")
        if resultado + 10 > 21:
            resultado = 1
            print("el Crupier elige valor 1")
        elif resultado == 10:
            print("el crupier elige valor 10")

    print("la carta tiene un valor de ", resultado)

def cartas():
    carta=randrange(51)

# Tirada Crupier
def tiradacartacrupier(lista, posicion, puntosjugador, puntoscrupier):
    plantado = False
    while puntoscrupier < puntosjugador:
        puntoscrupier += puntoscrupier + tomarcartacrupier(lista, posicion, puntosjugador, puntoscrupier)
        print("la puntuación del Crupier es ", puntoscrupier)
        sleep(1)

    if puntoscrupier >= puntosjugador and puntoscrupier < 22:
        print("PERDISTE! Gana el Crupier")
    else:
        print("HAS GANADO LA MANO!")
    return (puntoscrupier)


# Algoritmo principal
baraja = [int() for ind0 in range(52)]

# Iniciar la baraja
for i in range(52):
    baraja[i] = 0

crearbaraja(baraja)
print(baraja)

# Mezclar la baraja
for i in range(52):
    mezclarbaraja(baraja)
print(baraja)

# tomar carta
print("tomo carta")
puntos = 0
puntoscrupier = 0
puntosjugador = 0
print(tiradajugador(baraja, puntos))
if puntos < 21:
    tiradacartacrupier(baraja, randrange(51), puntos, puntoscrupier)
