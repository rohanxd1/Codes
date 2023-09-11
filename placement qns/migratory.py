ar=[1,4,4,4,5,3,7]
ar2=[0]*(max(ar)+1)
# print(ar2[:])
for elem in ar:
    ar2[elem]+=1
# print(ar2[:])
print(max(ar2))
print(ar2.index(max(ar2)))

