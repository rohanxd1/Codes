n=5
arr=[0]*n
arr = [-4, 3, -9, 0, 4, 1]
#copy
length=len(arr)
pos=0
neg=0
zero=0
for i in arr:
    if i==0:
        zero+=1
    elif i<0:
        neg+=1
    else:
        pos+=1
print(f"{pos:.6f}")
print(f"{(neg/n):.6f}")
print(f"{(zero/n):.6f}")
