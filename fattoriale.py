#!/usr/bin/env python3

# ESERCIZIO:
# definire la funzione fattoriale sia ricorsivamente che iterativamente

# definizione ricorsiva (quella "matematica")

def fucktorial(n):
	return 1 if n==0 else fucktorial(n-1)*n

# definizione iterativa

def f_iter(n):
	def iterazione(acc,i):
		if i == n:
			return acc
		return iterazione(acc*(i+1),i+1)
	return iterazione(1,0)

#print(f_iter(4))
