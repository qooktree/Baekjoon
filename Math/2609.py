import math
G,D=map(int,input().split())
a=math.gcd(G,D)
b=(G*D)//a
print(a)
print(b)
