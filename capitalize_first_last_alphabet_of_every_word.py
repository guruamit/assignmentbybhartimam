# Python program to capitalize the first and last character of each word in a string (input string should be a statement)
str1=input(str("Enter the sentence you want to modify :"))
str1 = str1.title()
str = str1.split()
str2 = ""

for i in str:
    str2 += i[:-1] + i[-1].upper()+" "
    print(str2)
print(str2)