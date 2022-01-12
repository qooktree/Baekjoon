while True:
  try:
    a=int(input())
    le='1'
    while True:
      if int(le)%a==0:
        print(len(le))
        break
      le+='1'
  
  except EOFError:
    break
