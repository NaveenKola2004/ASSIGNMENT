# Problem 1: Sum of Natural Numbers

def sum_nat_num(n):
    sum=0
    i=0
    while (i<n):
        i=i+1
        sum=sum+i
    print(sum)

number=int(input("Enter the number : "))

sum_nat_num(number)

# Problem 2: Count the Digits

def count_digit(num):
    store=[]
    i=0
    while (i<num):
        i=i+1
        store.append(i)
    print(store,len(store))
number=int(input("Enter the number : "))
count_digit(number)

# Problem 3: Reverse a Number

def reverse(n):
    reverse=0
    while (n>0):
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    print(reverse)
number=int(input("Enter the number : "))
reverse(number)

# Problem 4: Check for Palindrome Number

def reverse(n):
    reverse=0
    while (n>0):
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    return reverse
number=int(input("Enter the number : "))

num=reverse(number)

if (number==num):
    print("poli")
else:
    print("not poli")

# Problem 5: Print Digits of a Number

def digit_of_number(n):
  while (n>0):
     digit =n%10
     print(digit)
     n=n//10

number=int(input("Enter the number : "))
digit_of_number(number)

# Problem 6: Sum of Digits

def sum_of_digit(n):
    sum=0
    while (n>0):
        digit=n%10
        sum=sum+digit
        n=n//10
    print(sum)
sum_of_digit(456)

# Problem 7: Count Even and Odd Digits

def Odd_Even_count(n):
 odd=[]
 even=[]
 while(n>0):
    digit=n%10
    if (digit%2==0):
        even.append(digit)
    else:
        odd.append(digit)
    n=n//10
 print(odd,even)
 print("Even Digits : ",len(even))
 print("Odd Digits : ",len(odd))

number=int(input("Enter the number : "))
Odd_Even_count(number)

# Problem 8: Factorial of a Number

def factorial(n):
    i=1
    fact=1
    while(i<n+1):
        fact=fact*i
        i=i+1
    print(fact)
number=int(input("Enter the number : "))
factorial(number)
#2
def fact(n):
    if (n==0):
        return 1
    else:
        return n * fact(n-1)
number = int(input("Enter the number : "))
print(fact(number))

# Problem 9: Power of a Number

def power_of_number(base,Exponent):
    while (base>0):
        return base**Exponent
    else:
        return 1
base=int(input("Enter the Base : "))
exponent=int(input("Enter the Exponent : "))
print(power_of_number(base,exponent))

# Problem 10: Print Multiplication Table

def Multi_table(n):
 i=1
 while (i<11):
     print(f"{n}  X  {i} = {n*i}")
     i=i+1
number=int(input("Enter the number : "))
Multi_table(number)