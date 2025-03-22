#1. Check if a List is Empty

list=input("Enter the values : ").split()

if(list==[]):
    print("list is empty")
else:
    print("list is not empty")

list=[1,2,3]

if(len(list)==0):
    print("list is empty")
else:
    print("list is not empty")


#2. Check if a String Contains Only Digits

value=input()
check=value.isdigit()
if(check==True):
    print("Contains only digits")
else:
    print("Contains non-digit characters")

#3. Check if a Key Exists in a Dictionary

value={"name": "Alice", "age": 25}

if("name" in value):
    print("Key exists")
else:
    print("Key does not exist")

#4. Compare Two Lists for Equality
list=[1,2,3]
list2=[1,2,3]

if(list==list2):
    print("Lists are equal")
else:
    print("Lists are not equal")

#5. Find the Length of a String and Check its Category

value=input("Enter the value : ")

if(len(value)<5):
    print("Short")
elif(len(value)>=5 and len(value) <=10):
    print("Medium")
else:
    print("Long")


#6. Check if a List has Duplicates

value=[1,2,3,2]

count=value.count(2)
print(count)
if(count<=1):
    print("No duplicates found")
else:
    print("Duplicates found")

#7. Check if a String is a Valid Password

password=input()

if(len(password)<8):
    print("invalid")
elif not('1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password or '0' in password):
    print("invalid")
elif not('@' in password or '!' in password or '#' in password):
    print("invalid")
else:
    print("valid")

#8. Check if a Dictionary Contains a Specific Value

key={"name": "John", "age": 30}
value="Joh"
if(value in key.values()):
    print("value exists")
else:
    print("value not exist")

#10. Check if a List Contains Only Strings

list=["apple", "banana", "cherry",5]

if(5 in list):
    print("Not all elements are strings")
else:
    print("All elements are strings")