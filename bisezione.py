#!/usr/bin/env python3

# definizione della funzione di ricerca per bisezione
def CercaRadice(x,n,a,b,precisione):
	# scegliere a < b !
	if a > b:
		return "deve essere a < b"
	# se uno degli estremi è la radice, restituisci quello
	if a**n == x:
		return a
	if b**n == x:
		return b
	# calcola la media di a e b
	m = (a+b)/2
	# se la media è la radice, restituisci quella
	if m**n == x:
		return m
	# se la differenza tra b e a è inferiore ad una soglia, restituisci la loro media
	if b-a < precisione:
		return m
	# altrimenti, la funzione richiama se stessa
	if a**n < x and m**n > x:
		return CercaRadice(x,n,a,m,precisione)
	if m**n < x and b**n > x:
		return CercaRadice(x,n,m,b,precisione)

print(CercaRadice(3,3,1,3,10**-4))

