import sys
import math
input=sys.stdin.readline
M,N=map(int,input().split())

def is_prime(n):
  for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
      return False
  return True

for i in range(M,N+1):
  if i==1:
    continue
  elif is_prime(i)==True:
    print(i)
  else:
    continue
