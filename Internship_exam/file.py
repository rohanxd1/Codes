#4.File Handling: Write a Python program to read a text file and count the occurrences of each
#word, then display the words along with their counts
import string
f1=open("sample.txt","r+")
text=""
str1=""
word=0
l2=[]
wordlist=[]
for i in f1:
    text=i
f1.close
for i in text:
    if i!='.':
     str1=str1+i
    if i==" " or i=='.':
        wordlist.append(str1.strip())
        str1=" "
for i in wordlist:
   if i not in l2:  
      l2.append(i)
for i in l2:
    print(f"{i} = {wordlist.count(i)}")