#celsius to fahrenheit table
print('Celsius   Fahrenheit')
f=0
for i in range(0,101,10):
    print('  ',i,'\t     ',end='')
    f=(i*(9/5))+32
    print(f,end='\n')
