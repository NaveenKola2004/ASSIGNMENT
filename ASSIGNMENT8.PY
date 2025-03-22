#1. Check if a String is Empty

value=input("Enter the word : ")

if(value==""):
    print("STRING IS EMPTY")
else:
    print("NOT EMPTY")

#2. Check if a String Starts with a Vowel

vowels=('a','e','i','o','u')
value=input("Enter the word : ")

if (value.startswith(vowels)):
    print("Starts with vowel")
else:
    print("Does not starts with vowel")

#3. Determine the Length of a String

value=input("Enter tghe word : ")
length=len(value)

if (length <=5):
    print("Length is 5 or less")
else:
    print("Length is is more then 5")

# 4. Check if a String is a Single Character

value=input("Enter the word : ")
length=len(value)

if (length==1):
    print("Single character")
else:
    print("More then one character")

# 5. Check if a String Contains Only Alphabets

value=input("Enter the word : ")
alpha=value.isalpha()

if(alpha is True):
    print("Contains only alphabets")
else:
    print("Contains non-alphabet characters")

# 6. Check if a String is a Valid Email

mail=input("Enter your email : ")
symbol1='@'
symbol2='.'
if (symbol1 and symbol2 in mail):
    print("Valid email")
else:
    print('Invalid email')

# 7. Check if a String is in Uppercase or Lowercase

value=input("Enter tha word : ")
upper=value.upper()
lower=value.lower()

if(value==upper):
    print("Uppercase")
elif(value==lower):
    print("Lowercase")
else:
    print("mixed case")

# 8. Check if a String Ends with a Specific Suffix

value=input("Enter the word : ")
ends=value.endswith("ing")

if(ends==True):
    print("Ends with 'ing' ")
else:
    print("Does not ends with 'ing' ")

# 9. Compare Two Strings

word1=input("Enter the word : ")
word2=input("Enter the word : ")

if(word1==word2):
    print("Strings are Equal")
else:
    print("Strings are not Equal")

# 10. Check if a String is a Palindrome

value=input("Enter the word : ")
reverse=value[::-1]
if(reverse == value):
    print("Palindrome")
else:
    print("Not a palindrome")


j_angry=False
s_angry=False

if(j_angry == True and s_angry==True):
    print("so you are in trouble")
elif(j_angry ==False and s_angry==False):
    print("so you are in trouble")
else:
    print("so we are not in trouble")