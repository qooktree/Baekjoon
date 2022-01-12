import sys
input=sys.stdin.readline

X,Y,W,S=map(int,input().split())

move1=(X+Y)*W
if (X+Y)%2==0:
  move2=max(X,Y)*S
else:
  move2=(max(X,Y)-1)*S+W

move3=(min(X,Y)*S)+((max(X,Y)-min(X,Y))*W)

result=min(min(move1,move2),move3)
print(result)
