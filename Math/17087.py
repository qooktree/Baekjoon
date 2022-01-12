import sys
import math

n,s=map(int, input().split())
a=list(map(int,input().split()))
dif=list(set(abs(a[i]-s) for i in range(n)))
d=min(dif)
for i in range(len(dif)):
  d=math.gcd(dif[i],d)

print(d)
