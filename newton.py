#!/usr/bin/env python3

def newton(x,a,epsilon):
	if abs(x-a**2) < epsilon:
		return a
	return newton(x,(a+x/a)/2,epsilon)

print(newton(2,1,10**-7))

