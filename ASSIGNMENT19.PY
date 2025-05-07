#  Problem 1: Multiply Two Numbers

def multiply_two_Numbers(a,b):
    return a*b
a=int(input("enter the number : "))
b=int(input("Enter the number : "))
print(multiply_two_Numbers(a,b))

# Problem 2: Convert Minutes to Seconds

def seconds(hour):
    return hour*60
print(seconds(5))

# Problem 3: Greet a User

def Greet(name):
    return (f"Hello, {name}")
name=input("Enter you name : ")
print(Greet(name))

# Problem 4: Absolute Difference from 21

def diff21(n):
    if (n>21):
        return (n-21)*2
    else:
        return 21-n
n=int(input("Enter the number : "))
print(diff21(n))

# Problem 5: Calculate Total Bill with Tip

def total_bill(bill_amount,tip_amount):
    return float(bill_amount+tip_amount)
bill_amount=float(input("Enter the bill amount : "))
tip_amount=int(input("Enter the tip amount : "))
print(total_bill(bill_amount,tip_amount))

# Problem 6: Remove Vowels

# Problem 7: Is Even
def Is_Even(n):
    if n%2==0:
        return True
    else:
        return False
number=int(input("Enter the number : "))
print(Is_Even(number))

# Problem 8: Sum of Digits

def Sum_Of_Digits(n):
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
number=int(input("Enter trhe n number : "))
print(Sum_Of_Digits(number))

# Problem 9: Find Unique Elements

def unique_elements(a):
    elements=[]
    normal=[]
    for i in a:
        if a.count(i)==1:
            elements.append(i)
        else:
            normal.append(i)
    return elements
print(unique_elements([1,2,2,3,4,4,5]))

# Problem 10: All Permutations of a String
# Problem 11: Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
print(longest_word("I love artificial intelligence"))

# Problem 12: Recursive Power Function

def power(base,exp):
    return base**exp
print(power(2,3))