#!/usr/bin/env python3

# ESERCIZIO
# implementare una funzione che dice se un numero è primo o no

def IsPrime(n):
	def exaustive(i):
		if i*i > n: # ricerca divisori tra gli interi compresi tra i al quadrato e n
			return True # inutile cercare divisori di n maggiori di √n (se ci fosse un divisore > √n ci sarebbe anche divisore < √n)
		if n%i == 0: # se i divide n, allora n sicuramente non primo
			return False # fine!
		return exaustive(i+1) # altrimenti prova sul successivo
	return exaustive(2) # voglio che la funzione IsPrime faccia questo!

#print(IsPrime(7))
