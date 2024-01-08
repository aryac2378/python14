names = eval(input("Enter list: "))
max_length = 0

for i in names:
    if len(i) > max_length:
        max_length = len(i)

print("Maximum length:", max_length)
