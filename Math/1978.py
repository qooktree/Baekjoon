import sys
import math

def is_prime(n):
  for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
      return False
  return True

input=sys.stdin.readline
N=int(input())
nums=map(int,input().split())

result=0
for i in nums:
  if i==1:
    continue
  elif is_prime(i)==True:
    result+=1
  else:
    continue
print(result)
