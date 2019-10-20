#!/usr/bin/env python3

# ESERCIZIO
# implementare una funzione che dice se un numero è primo o no

def IsPrime(n):
	# leggi la fine di questo blocco prima!
	def exaustive(i):
		# inutile cercare divisori di n maggiori della radice quadrata di n (= sqrt(n))
		# infatti: se ci fosse un divisore maggiore di sqrt(n),
		# ci sarebbe anche divisore minore di sqrt(n) [da riscrivere meglio]
		if i*i > n:
		# al posto di "i*i" puoi mettere "i",
		# ma l'algoritmo risultarà molto lento e occupa più memoria
			return True
		# se i divide n, allora n sicuramente non primo
		if n%i == 0:
			return False
		# altrimenti prova sul successivo
		return exaustive(i+1)
	# voglio che la funzione IsPrime faccia questo!
	return exaustive(2)

#print(IsPrime(111213141))
