#!/usr/bin/env python3

def m(a,b):
	return (a+b)/2

def bisezione(a,b):
	if abs(a-b) < 0.001:
		return m(a,b)
	if a*a<2 and m(a,b)*m(a,b)>2:
		return bisezione(a,m(a,b))
	else:
		return bisezione(m(a,b),b)

print(bisezione(1,2))
