def valoremonete(a,b,c,d):
    return (a+2*b+5*c+10*d)
def cambio(a,b,c,d,x,):
    if valoremonete(a,b,c,d)==50:
        x=x+1
    if d==5:
        print (x)
    elif valoremonete(0,0,c,d)>=50:
        cambio(0,0,0,d+1,x)
    elif valoremonete(0,b,c,d)>=50:
        cambio(0,0,c+1,d,x)
    elif valoremonete(a,b,c,d)>=50:
        cambio(0,b+1,c,d,x)
    else:
        cambio(50-(2*b+5*c+10*d),b,c,d,x)
        
cambio(0,0,0,0,0)