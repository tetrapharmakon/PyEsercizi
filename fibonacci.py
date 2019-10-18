#!/usr/bin/env python3

# ESERCIZIO:
# implementare la funzione di fibonacci sia ricorsivamente che iterativamente

# definizione ricorsiva

def fib1(n):
	if n <= 1:
		return n
	return fib1(n-1)+fib1(n-2)

# definizione iterativa [da trovare ancora...]
