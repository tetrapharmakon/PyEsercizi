#!/usr/bin/env python3

# ESERCIZIO:
# scrivere funzione che calcolano la somma e il prodotto
# di due numeri naturali x e y usando solamente le seguenti funzioni

# funzione incremento
def inc(x):
	return x+1

# funzione decremento
def dec(x):
	return x-1

# la funzione che calcola la somma
def somma(x,y):
	if y == 0:
		return x
	return inc(somma(x,dec(y)))

# la funzione che calcola il prodotto
def prodotto(x,y):
	if y == 0:
		return 0
	return somma(prodotto(x,dec(y)),x)

# definizione alternativa della funzione prodotto
def ProdottoAlternativo(x,y):
	# usiamo una "funzione interna"
	# questa non fa altro che decrementare y ed aggiungere x ad acc
	# ogni volta che è chiamata
	def FunzioneInterna(y,acc):
		if y == 0:
			return acc
		return FunzioneInterna(y-1,acc+x)
	# l'idea è di partire con acc = 0
	return FunzioneInterna(y,0)

