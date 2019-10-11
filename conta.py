#!/usr/bin/env python3

# Esercizo: conteggio da x a y
# stampa uno per linea i numeri interi da x a y

def conta(x,y):
	print(x)
	if x < y:
		conta(x+1,y)

conta(1,10)
