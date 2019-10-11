#!/usr/bin/env python3

# Esercizio:
# scrivere funzione che calcolano la somma e il prodotto
# di due numeri naturali x e y usando solamente le seguenti funzioni

def inc(x):
	return x+1

def dec(x):
	return x-1

# la funzione che calcola la somma
def somma(x,y):
	if y == 0:
		return x
	else:
		return inc(somma(x,dec(y)))

# la funzione che clacola il prodotto
def prodotto(x,y):
	if y == 0:
		return 0
	else:
		return somma(prodotto(x,dec(y)),x)

