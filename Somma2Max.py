#!/usr/bin/env python3

# ESERCIZIO:
# dati tre numeri, definire una funzione che prende i due numeri più grandi
# per poi sommarne i quadrati

# IMPLEMENTAZIONE PIÙ SEMPLICE
def Somma2Max(x,y,z):
	if x <= y and x <= z:
		return y**2+z**2
	if y <= x and y <= z:
		return x**2+z**2
	return x**2+y**2


# IMPLEMENTAZIONE ALTERNATIVA
# IDEA: sommare i quadrati dei tre numeri e togliere il quadrato del numero più piccolo
# per trovare il minimo di tre numeri x ,y e z possiamo fare così:
# * prendere i primi due numeri e trovarne il minimo, chiamiamolo m
# * calcolare il minimo tra m e z: questo sarà il più piccolo dei tre

# definiamo una funzione che trova il minimo di due numeri
def min2(x,y):
	if x <= y:
		return x
	else:
		return y

# ora il minimo dei tre elementi
def min3(x,y,z):
	return min2(min2(x,y),z)

# la funzione che cercavamo!
def f(x,y,z):
	return x**2+y**2+z**2-min3(x,y,z)**2
