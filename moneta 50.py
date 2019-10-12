def valoremonete(a,b,c,d):
    return (a+2*b+5*c+10*d)
def cambio(a,b,c,d,x):
    if valoremonete(a,b,c,d)==20:
        x=x+1
    if d==2:
        print (x)
    elif c==4:
        cambio(0,0,0,d+1,x)
    elif b==10:
        cambio(0,0,c+1,d,x)
    elif a==20:
        cambio(0,b+1,c,d,x)
    else:
        cambio(a+1,b,c,d,x)
        
cambio(0,0,0,0,0)