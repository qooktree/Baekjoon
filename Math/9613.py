import sys
import math
input=sys.stdin.readline
t=int(input())

for i in range(t):
  n=list(map(int,input().split()))
  total=0
  for j in range(1,len(n)):
    for k in range(j+1,len(n)):
      total+=math.gcd(n[j],n[k])
  print(total)
