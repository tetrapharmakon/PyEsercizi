#!/usr/bin/env python3

# ESERCIZIO:
# definire ricorsivamente la funzione potenza con esponente naturale

def potenza(x,n):
	if n == 0:
		return 1
	return potenza(x,n-1)*x

#print(potenza(2,5))

# ESERCIZIO ***
# definire iterativamente la funzione potenza

def esponenziale(x,n):
	def iterazione(acc,i):
		if i == n:
			return acc
		return iterazione(acc*x,i+1)
	return iterazione(1,0)

#print(esponenziale(3,4))
