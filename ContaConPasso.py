#!/usr/bin/env python3

# ESERCIZIO:
# conteggio dall'intero a all'intero b con passo p

def ContaConPasso(a,b,p):
	return range(a,b+1,p) if a <= b else []
