#!/usr/bin/env python3

# ESERCIZIO: ricerca con la "forza bruta"
# Implementare un algoritmo di ricerca che trovi la radice intera di x
# nell'insieme { 0, 1, 2, 3, ..., x }

def CercaRadiceQuadrata(x):
	def FunzioneInterna(n):
		if n == 0:
			return "non ho trovato niente!"
		else:
			if x == n**2:
				return n
			return FunzioneInterna(n-1)
	return FunzioneInterna(x)

print(CercaRadiceQuadrata(9))
