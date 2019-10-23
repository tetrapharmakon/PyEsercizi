#!/usr/bin/env python3

# ESERCIZIO:
# implementare la funzione di fibonacci sia ricorsivamente che iterativamente

# definizione ricorsiva

def fib1(n):
	if n <= 1:
		return n
	return fib1(n-1)+fib1(n-2)

# definizione iterativa

def fib2(n):
	def iterazione(a,b,i):
		if i == n:
			return a
		return iterazione(a+b,a,i+1)
	return iterazione(0,1,0)

#print(fib1(4),fib2(4))
