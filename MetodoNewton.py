#!/usr/bin/env python3

# ESERCIZIO:
# ricerca di soluzioni approssimate della radice quadrata
# attraverso il metodo di Newton

def newton(x,a,epsilon):
	if x-a**2 > -epsilon and x-a**2 < epsilon:
		return a
	return newton(x,(a+x/a)/2,epsilon)

#print(newton(2,1,10**-7))

