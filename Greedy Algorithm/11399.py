N=int(input())
p=list(map(int,input().split()))
p.sort()
count=0
round=N
for i in range(len(p)):
  count+=p[i]*round
  round-=1

print(count)
