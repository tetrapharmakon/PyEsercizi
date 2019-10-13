
def valoremonete(a,b,c,d):
    return (a+2*b+5*c+10*d)

def cambio(a,b,c,d,x):
<<<<<<< HEAD:moneta50.py
	if valoremonete(a,b,c,d)==50:
		x=x+1
    if d==5:
		print(x)
	elif valoremonete(0,0,c,d)>=50:
		cambio(0,0,0,d+1,x)
	elif valoremonete(0,b,c,d)>=50:
		cambio(0,0,c+1,d,x)
    elif valoremonete(a,b,c,d)>=50:
		cambio(0,b+1,c,d,x)
	else:
		cambio(50-(2*b+5*c+10*d),b,c,d,x)

=======
    if valoremonete(a,b,c,d)==20:
        x=x+1
    if d==2:
        print (x)
    elif valoremonete(0,0,c,d)>=20:
        cambio(0,0,0,d+1,x)
    elif valoremonete(0,b,c,d)>=20:
        cambio(0,0,c+1,d,x)
    elif valoremonete(a,b,c,d)>=20:
        cambio(0,b+1,c,d,x)
    else:
        cambio(20-(2*b+5*c+10*d),b,c,d,x)
        
>>>>>>> 31a37e1fa6f4be557cbc0fa6217066181c177b69:moneta20.py
cambio(0,0,0,0,0)
