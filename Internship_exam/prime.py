#2.write a python program to find if the given number is prime or not
a= int(input("Enter number:"))
if a==1:
    print("prime")
elif a==2:
    print("prime")
elif a==4:
    print("Not Prime") # because of way for loop was stated
else :
    mid=a//2
    flag=True
    for i in range(2,mid):
        if a%i==0:
            flag=False
            break
    if flag==True:
        print("Prime")
    else:
        print("Not Prime")
        