#!/usr/bin/env python3

# media di sue numeri
def m(a,b):
	return (a+b)/2

# definizione della funzione di ricerca per bisezione
def CercaRadice(x,n,a,b,precisione):
	# scegliere a < b !
	# se uno degli estremi è la radice, restituisci quello
	if a**n == x:
		return a
	if b**n == x:
		return b
	# se la media è la radice, restituisci quella
	if m(a,b)**n == x:
		return m(a,b)
	# se la differenza tra b e a è inferiore ad una soglia, restituisci la loro media
	if b-a < precisione:
		return m(a,b)
	# altrimenti, la funzione richiama se stessa
	if a**n < x and m(a,b)**n > x:
		return CercaRadice(x,n,a,m(a,b),precisione)
	if m(a,b)**n < x and b**n > x:
		return CercaRadice(x,n,m(a,b),b,precisione)

#print(CercaRadice(3,3,1,3,10**-4))

