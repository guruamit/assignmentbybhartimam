# Python program to count the number of vowels in a given string.
str1=input(str("Enter the string you want to count the vowel of :"))
temp= " "
counter=0
list1=["A","E","I","O","U","a","e","i","o","u"]
for i in str1 : 
    if i in list1:
        counter = counter+ 1
        if i in temp :
            counter = counter -1
        else :
             temp = temp +i
    
print(counter)  
print("Thank you") 