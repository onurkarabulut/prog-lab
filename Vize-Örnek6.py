# NxN karakteri NxN matrise atama

import math
a="ONURONURONURONUR"

def fonk(kel):
    b=[]
    x=0
    b=list(kel)
    n=int(math.sqrt(len(b)))
    c=[]
    for i in range(n):
        c.append([])
        for j in range(n):
            c[i].append(b[x])
            x+=1
    return c

print(fonk(a))
    
            
