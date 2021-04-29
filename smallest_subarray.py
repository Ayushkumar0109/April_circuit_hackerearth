n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    y=input().split()
    if y[0]=='pop':
        s.pop(int(y[1]))
    if y[0]=='remove':
        s.remove(int(y[1]))
    if y[0]=='discard':
        s.discard(int(y[1]))
    print(s)
sum=0
for i in s:
    sum=sum+i
print(sum)                    
        
        
