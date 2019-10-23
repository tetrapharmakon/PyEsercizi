#!/usr/bin/env python3

# ESERCIZIO:
# conteggio dall'intero a all'intero b con passo p

def ContaConPasso(a,b,p):
	if a <= b:
		print(a)
		ContaConPasso(a+p,b,p)

ContaConPasso(2,9,4)

