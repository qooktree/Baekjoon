N=int(input())

time=[[0]*2 for _ in range(N)]

for i in range(N):
  s,e=map(int,input().split())
  time[i][0]=s
  time[i][1]=e

time.sort(key=lambda x:(x[1],x[0]))

e_time=time[0][1]
answer=1

for i in range(1,N):
  if time[i][0]>=e_time:
    answer+=1
    e_time=time[i][1]

print(answer)
