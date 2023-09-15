arr=[1,3,5,7,9]
#copy
length=len(arr)
asc=sorted(arr)
desc=sorted(arr,reverse=True)
max=0
min=0
for i in range(0,length-1):
    min=asc[i]+min
    max=desc[i]+max
print(f"{min} {max}")