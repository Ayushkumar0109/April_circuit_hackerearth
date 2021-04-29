n=int(input())
from collections import OrderedDict
c=[]
l=[]
d=OrderedDict()
for i in range(n):
    a,b=input().split()
    d[a]=int(b)
for a,b in enumerate(d):
    if b not in c:
        c.append(b)
for i in c:
    val=0
    for k,v in enumerate(d):
        if v==i:
            val=val+d[v]
            print(val)
    l.append(val) 
    print(val)       
for i in range(len(c)):
    print(c[i],end=' ')
    print(l[i])
                    
                
            
    
