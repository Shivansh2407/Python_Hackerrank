import re
n=input()
l=list(n)
if(re.match("^[1-9]{2}[A-Z][1-9]{3}-[1-9]{2}",n)):
    if(l[2]=="A" or l[2]=="E" or l[2]=="I" or l[2]=="O" or l[2]=="U" or l[2]=="Y"):
        print("invalid")
    else:
        if((int(l[0])+int(l[1]))%2==0):
            print("valid")
        elif((int(l[0])+int(l[1])%2==0 )):
            print("valid")
        elif((int(l[0])+int(l[1])%2==0 )):
            print("valid")  
        elif(((int(l[0])+int(l[1]))%2==0)):
            print("valid")
        else:
            print("invalid")
