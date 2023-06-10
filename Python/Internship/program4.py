#accept num >10 then print all odd nums
flag=True
while flag==True :
 n=int(input('Enter num greater than 10:'))
 if n>10:
     flag=False
     for i in range(1,n+1):
         if i%2!=0 :
             print(i,'',end='')
 else:
     print("Number less than 10")