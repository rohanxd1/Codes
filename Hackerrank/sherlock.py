n=13
ss=''
if n%3==0:
        ss+='5'*n
        print(ss)
elif n%5==0:
        ss+='3'*n
        print(ss)
elif (n-5)%3==0:
        ss+='5'*(n-5)
        ss+='3'*5
        print(ss)
elif (n-3)%5==0:
        ss+='5'*3
        ss+='3'*(n-3)
        print(ss)
else:
      print(-1)
