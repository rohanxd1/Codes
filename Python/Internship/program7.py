print('Enter values (press 0 to exit)')
count=1
n=int(input(''))
sum=n
avg=n
if n!=0: 
    while(n!=0):
        n=int(input(''))
        count+=1
        sum=sum+n
        avg=sum/count
        if n==0:
            break
    print('avg=',avg)
else:
    print("Error First number cannot be 0")
