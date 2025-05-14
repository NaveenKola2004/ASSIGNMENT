# 🔰 Problem 1: Even or Odd Checker

def Even_Odd_Check(n):
    if n%2==0:
        print(f"{n} is even Number")
    else:
        print(f"{n} is odd Number")
Number=int(input("Enter the number : "))
Even_Odd_Check(Number)

# 🔰 Problem 2: Sum of First N Natural Numbers

def Sum_N_numbers(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    print(sum)
Number=int(input("Enter the number : "))
Sum_N_numbers(Number)

# 🔰 Problem 3: Find Maximum of Three Numbers

def Find_Max_Number(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(num1)
        else:
            print(num3)
    else:
        if num2>num3:
            print(num2)
        else:
            print(num3)
num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
Find_Max_Number(num1,num2,num3)

# 🔰 Problem 4: Count Vowels in a String

def Count_Vowels(word):
    Total_vowels=0
    seperated_word=[]
    vowels=["a","e","i","o","u"]
    while word:
        last_word=word[-1]
        last_word=last_word.lower()
        seperated_word.append(last_word)
        if last_word in vowels:
            Total_vowels=Total_vowels+1
        word=word[:-1]
    print(Total_vowels)
Count_Vowels("NAVEEN")

# 🔰 Problem 5: Print Multiplication Table

def Tables(number):
    i=1
    while i<=10:
        print(f"{number} X {i}= {i*number}")
        i=i+1
n=int(input("Enter the number : "))
Tables(n)

# 🔰 Problem 6: Check Prime Number

def Prime_Number_Check(n):
    if n<=1:
        print("Prime number")
    else:
        i=2
        is_prime=True
        while i<=n //2:
            if n%i==0:
                is_prime=False
                break
            i=i+1
    
    if is_prime:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")
Prime_Number_Check(7)

#🔰 Problem 7: Reverse a String

def reverse_string(word):
    print(word[::-1])
word=input("Enter the string : ")
reverse_string(word)

# 🔰 Problem 8: Factorial of a Number

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("Enter the number : "))
print(factorial(number))

# 🔰 Problem 9: Check Palindrome

def palindrome(word):
    reverse=word[::-1]
    if word==reverse:
        print("It is palindrome")
    else:
        print("it is not palindrome")
string=input("Enter the word : ")
palindrome(string)

# 🔰 Problem 10: Count Digits in a Number

def Count_Digit(n):
    number=str(n)
    print(len(number))
number=int(input("Enter the number : "))
Count_Digit(number)

# 🔰 Problem 11: Check Leap Year
def Leap_Check(year):
    if year%4==0 and year%100!=0:
        print(f"{year} Leap year")
    else:
        print(f"{year} It is not leap year")
year=int(input("Enter the year : "))
Leap_Check(year)

# 🔰 Problem 12: Sum of Even Numbers in a List

def Sum_Evennumber_List(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum)
numbers=[]
n=int(input("How my numbers to to add list : "))
for i in range(1,n+1):
    number=int(input(f"Enter the even numbers {i} : "))
    numbers.append(number)
Sum_Evennumber_List(numbers)
# SUM OF BOTH EVEN AND ODD

def Sum_Evennumber_List(list):
    Sum_Evennumbers=0
    Sum_Oddnumbers=0
    Even_numbers=[]
    Odd_Numbers=[]
    for i in list:
        if i%2==0:
            Even_numbers.append(i)
        else:
            Odd_Numbers.append(i)
    for k in Even_numbers:
        Sum_Evennumbers=Sum_Evennumbers+k
    for j in Odd_Numbers:
        Sum_Oddnumbers=Sum_Oddnumbers+j
    print(f"Even numbers in list {Even_numbers} Sum is = {Sum_Evennumbers}\nOdd numbers in list {Odd_Numbers} sum is = {Sum_Oddnumbers}")        
numbers=[]
n=int(input("How my numbers to to add list : "))
for i in range(1,n+1):
    number=int(input(f"Enter the even numbers {i} : "))
    numbers.append(number)
Sum_Evennumber_List(numbers)
