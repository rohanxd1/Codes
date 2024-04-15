#1.write a python program to count the number of Occurances of each Character in a String

a=input("Enter string:")
l1=[]
l2=[]
for i in a:
    if i not in l1:
        l1.append(i)
        occur=a.count(i)
        l2.append(occur)
for i in range(len(l1)):
    print(f"{l1[i]} occured {l2[i]} times")
