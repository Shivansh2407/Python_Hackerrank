n=input()
count=0
a=set(input())
b=(input()).split()
c=(input()).split()
for i in range (0,len(b)):
    if(b[i] in a ):
        count=count+1
    else:
        break
for i in range (0,len(c)):
    if(c[i] in a ):
        count=count-1
    else:
        break
print(count)

