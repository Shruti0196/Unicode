from collections import Counter , OrderedDict
wordarray=[]           #input array of words
n=int(input("Enter number of words : "))
for i in range(n):
    wordarray.append(input().strip())
countdict=OrderedDict(Counter(wordarray))        #dictionary of number of occurences of words
l=len(countdict)
print("Number of distinct words : ",l)
print("Order of occurrences :",end=' ')
for word in countdict:
    print(countdict[word],end="\t")
keylist=list(countdict.keys())
valuelist=list(countdict.values())
for i in range(l-1):                            #conversion into descending order of keylist and valuelist
    for j in range(l-1):
        if (valuelist[j]<valuelist[j+1]):
            t1=valuelist[j]
            valuelist[j]=valuelist[j+1]
            valuelist[j+1]=t1
            t2=keylist[j]
            keylist[j]=keylist[j+1]
            keylist[j+1]=t2
print("\nDescending order of words :",end=' ')
if(l==n):
    print("Occurrence of all words is equal ",end='')
else:
    for text in keylist:
        print(text,end="\t")
count1=0
count2=0
for k in range(l):
    if(valuelist[k]==valuelist[0]):
        count1+=1

for s in range(l):
    if(valuelist[s]==valuelist[l-1]):
        count2+=1
print("\nMost repeated word :",end=' ')
for p in range(count1):
    print(keylist[p],end="\t")
print("\nLeast repeated word :", end=' ')
for q in range(count2):
    print(keylist[l-1-q], end="\t")



