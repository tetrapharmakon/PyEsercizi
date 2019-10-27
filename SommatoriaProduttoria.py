#!/usr/bin/env python3

# ESERCIZIO:
# Implementare le funzioni sommatoria e produttoria

def sommatoriaI(F,i,n):
	def somma(j):
		if j == i:
			return F(j)
		return somma(j-1)+F(j)
	return somma(n)

def sommatoriaII(F,i,n):
	def iterazione(s,j):
		if j == n+1:
			return s
		return iterazione(s+F(j),j+1)
	return iterazione(0,i)

def produttoriaI(F,i,n):
	def prodotto(j):
		if j == i:
			return F(j)
		return prodotto(j-1)*F(j)
	return prodotto(n)

def produttoriaII(F,i,n):
	def iterazione(p,j):
		if j == n+1:
			return p
		return iterazione(p*F(j),j+1)
	return iterazione(1,i)

