print('Enter 3 sides of a triangle:')
s1=int(input("side1="))
s2=int(input("side2="))
s3=int(input("side3="))
if s1==s2==s3:
    print("Equilateral")
elif s1==s2 or s2==s3 or s1==s3:
    print('Isosceles')
else:
    print('Scalene')