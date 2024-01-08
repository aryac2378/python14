def insertinmiddle(string1,insertstring):
    newstring=string1[0:int(len(string1)/2)]+insertstring+string1[int(len(string1)/2):]
    print(newstring)

string1=input("Enter string: ")
string2=input("Enter string to insert: ")
insertinmiddle(string1,string2)