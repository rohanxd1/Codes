n=9
binary=bin(n)
binary=binary[2:]
padding=32-len(binary)
binary='0'*padding+binary
print(binary)
flipped=''
for i in binary:
    i=int(i)
    value=i^1
    flipped+=str(value)
flipped=int(flipped,2)
print(flipped)

