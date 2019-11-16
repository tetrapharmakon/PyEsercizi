#!/usr/bin/env python3

# ESERCIZIO:
# implementare la funzione di fibonacci sia ricorsivamente che iterativamente

# definizione ricorsiva

# vorrei un analogo funzionale della definizione standard in Haskell:
# | feeb :: [Integer]
# | feeb = 1 : 1 : zipWith (+) feeb (tail feeb)
def feeb(n):
	fib_list = [ a+b | a in fib_list, b in fib_list[:1]]
	return fib_list[:n]

# chiaramente questo non funziona perché python non è lazy; dio che schifo python

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
