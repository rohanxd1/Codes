c=input("Enter number:")
print("reverse:",c[::-1])
if c==c[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")