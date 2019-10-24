#!/usr/bin/env python3

# ESERCIZIO:
# Implementare una funzione che sommi gli elementi di una lista

#from math import sqrt

def sommatoriaI(f,i,n):
	def somma(j):
		if j == i:
			return f(j)
		return somma(j-1)+f(j)
	return somma(n)

def sommatoriaII(f,i,n):
	def iterazione(s,j):
		if j > n:
			return s
		return iterazione(s+f(j),j+1)
	return iterazione(0,i)

#def pi(n):
#	return sqrt(6*sommatoriaII(lambda n: n**-2, 1, 100))

#print(pi(10))

