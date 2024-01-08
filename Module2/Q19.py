string1=input("Enter string: ")
notindex=string1.find("not")
poorindex=string1.find("poor")
if poorindex<notindex:
    newstring=string1[:poorindex]+"good"+string1[notindex+3:]
    print(newstring)
else:
    print(string1)