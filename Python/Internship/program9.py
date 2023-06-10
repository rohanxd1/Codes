def purchases(n):
    if n==1:
        shipping=10.95
    else:
        shipping=10.95+((n-1)*2.95)
    return shipping
n=int(input("Enter number of orders:"))
if n!=0:
    amount=purchases(n)
    print("Shipping charges=",amount)
else:
    print("Invalid input")
