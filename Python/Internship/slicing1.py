str='Hello World!'
for i in str:
    if i=='H' or i=='W':
        print(i,end='')
print(end='\n')
for i in str:
    if i=='o':
        print(i,end='')
print(end='\n')
x1=str[2:5]
x2=str[8:11]
print(x1+x2)
print(str[::-1])
print(str[6:12])
print(str[0:5])