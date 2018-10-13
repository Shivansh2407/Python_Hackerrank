def capitalize():
    r=n.split()
    b=""
    for i in range (0,len(r)):
        
        s=r[i].capitalize()
        b=b+" "+s
    k=b.strip()
    
    print(k)

n=input()
capitalize()
