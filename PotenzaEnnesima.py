#!/usr/bin/env python3

# ESERCIZIO:
# definire ricorsivamente la funzione potenza con esponente naturale

def potenza(x,n):
	if n == 0:
		return 1
	return potenza(x,n-1)*x

#print(potenza(2,5))
