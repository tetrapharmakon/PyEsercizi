#!/usr/bin/env python3

# ESERCIZIO
# implementare una funzione che dice se un numero è primo o no

def IsPrime(n):
	def exaustive(i):
		if i >= n: # ricerca divisori tra gli interi i < n
			return True # inutile cercare divisori di n sopra n
		if n%i == 0: # se i divide n, allora n sicuramente non primo
			return False # fine!
		return exaustive(i+1) # altrimenti prova sul successivo
	return exaustive(2) # voglio che la funzione IsPrime faccia questo!

#print(IsPrime(7))
