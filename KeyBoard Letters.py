row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

s = input("Enter your string>>>")

#converting string into lowercase
s = s.lower()

flag = True

#assuming that string only contains alphabets
#checking for the first character of the string
if s[0] in row1:
	for i in s:
		if i not in row1:
			flag = False
elif s[0] in row2:
	for i in s:
		if i not in row2:
			flag = False

elif s[0] in row3:
	for i in s:
		if i not in row3:
			flag = False

if flag == True:
	print( "Yes")
else:
	print ("No")
