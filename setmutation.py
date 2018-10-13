n = int(input())
count=0
s = set(map(int, input().split()))
m=int(input())
for i in range (0,m):
    l=input().split()
    if (l[0]=="intersection_update"):
        h=set(map(int, input().split()))
        s.intersection_update(h)
    elif (l[0]=="update"):
        k=set(map(int, input().split()))
        s.update(k)
    elif (l[0]=="symmetric_difference_update"):
        p=set(map(int, input().split()))
        s.symmetric_difference_update(p)
    elif (l[0]=="difference_update"):
        q=set(map(int, input().split()))
        s.difference_update(q)
for j in range (0,len(s)):
    count=count+int(list(s)[j])
print(count)
