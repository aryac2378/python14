string1=input("Enter string: ")
if len(string1)>2:
    newstring=string1[0:2]+string1[len(string1)-2:len(string1)+1]
else:
    newstring=''
print(newstring)