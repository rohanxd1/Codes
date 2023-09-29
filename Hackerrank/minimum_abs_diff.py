diff=[]
arr=[-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
arr.sort()
for i in range(len(arr)-1):
    diff.append(abs(arr[i]+-arr[i+1]))
print(min(diff))