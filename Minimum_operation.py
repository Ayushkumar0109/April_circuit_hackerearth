s ,n=input().split()
from itertools import combinations
i=1
while i<=int(n):
    for val in combinations(sorted(s),i):
        print(''.join(val))    
    i+=1    
