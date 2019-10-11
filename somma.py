#!/usr/bin/env python3

# Esercizio:
# Implementare una funzione che sommi gli elementi di una lista

def somma(lista):
	# una funzione interna così definita:
	# __somma__(0) = "primo elemento della lista"
	# __somma__(n) = __somma__(n-1)+"n-esimo termine della lista"
	def __somma__(n):
		if n == 0:
			return lista[0]
		else:
			return __somma__(n-1)+lista[n]
	if lista == []:
		return None
	else:
		# emetti il valore __somma__("lunghezza della lista"-1)
		return __somma__(len(lista)-1)

print(somma([1,2,3,4]))
