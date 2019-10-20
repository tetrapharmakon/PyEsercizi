#!/usr/bin/env python3

# ESERCIZIO:
# algoritmo di Euclide per il calcolo del massimo comun divisore di due numeri naturali

def MCD(a,b):
	if b == 0:
		return a
	return MCD(b,a%b)

print(MCD(15,17))
