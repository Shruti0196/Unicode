from collections import Counter , OrderedDict
wordarray=[]           #input array of words
n=int(input("Enter number of words : "))
for i in range(n):
    wordarray.append(input().strip())
countdict=OrderedDict(Counter(wordarray))        #dictionary of number of occurences of words
print(len(countdict))
for word in countdict:
    print(countdict[word],end="\t")
