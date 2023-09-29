s='The quick brown fox jumps over the lazy dog'
s2=s.lower()
alphabet=[]
for i in range(97,123):
    alphabet.append(i)
for item in s2:
    if ord(item) in alphabet:
        alphabet.remove(ord(item))

if len(alphabet)>0:
    print("Not Pangram")
else:
    print("Pangram")
