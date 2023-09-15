strings=['ab','ab','abc']
queries=['ab','abc','bc']

c=[]
for i in queries:
    count=strings.count(i)
    c.append(count)
print(c[::])
