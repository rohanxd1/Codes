arr=[1,3,5,7,9]
n=len(arr)
arr.sort()
min=sum(arr[0:len(arr)-1])
max=sum(arr[len(arr):0:-1])
print(f"{min} {max}")