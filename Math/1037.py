import math
N=int(input())
real=list(map(int,input().split()))

result=0
min=min(real)
max=max(real)

if len(real)==1:
  result=real[0]*real[0]
else:
  result=min*max

print(result)
