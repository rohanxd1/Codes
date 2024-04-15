#3. Write a python yprogram to count the number of vowels in a given string

a=input("Enter string:")
low=a.lower()
#l2=[]
occur=0
l1=["a","e","i","o","u"]   
for i in low:
    if i in l1:
        occur=occur+1
print(f"Total number of vowels:{occur}")
