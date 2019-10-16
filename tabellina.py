#!/usr/bin/env python3

# ESERCIZIO:
# stampa la tabellina di un numero naturale x

def tab(x):
	def rec(n):
		print(x*n)
		if n < 10:
			rec(n+1)
	rec(0)

tab(4)
