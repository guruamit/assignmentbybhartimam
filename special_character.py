# Program to check if a string contains any special character.
str1 =input(str("Enter the sentence you wan to check :"))
temp ="!@#$%^&*()_+=-,./?;:"
store = 0
for i in str1 :
    if i in temp:
        store = store +1
        # print("String is  not accepted")
    else :
        store = 0
        # print("String is accepted")    
if store >=1 :
    print("String is not accepted")   
else :
    print("String is accepted :") 
print("Thank you")        