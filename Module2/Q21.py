string1=input("Enter string1: ")
if len(string1)%4==0:
    newstring=string1[::-1]
    print(newstring)
else:
    print(string1)