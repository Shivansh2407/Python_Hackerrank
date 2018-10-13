def seqsearch(list,item):
    found=False
    for i in range(0,len(alist)):
        if(alist[i]==item):
            found=True
    return found
alist=input().split()
print(seqsearch(alist,input()))
