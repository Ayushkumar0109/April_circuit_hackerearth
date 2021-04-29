import math
ab=float(input())
bc=float(input())
s=ab**2+bc**2
ac=s**(1/2)
s1=bc**2-(ac/2)**2
mb=s1**(1/2)
theta=math.atan(ac/(2*mb))
print(round(math.degrees(theta)),end="°")


