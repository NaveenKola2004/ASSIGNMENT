# Problem 1: Print All Natural Numbers up to N
def All_Numbers(n):
 i=1
 while (i<n+1):
    print(i,end=" ")
    i=i+1
n=int(input("Enter the number : "))
All_Numbers(n)

# Problem 2: Print All Even Numbers up to N

def Even_Numbers(n):
    a=[]
    i=0
    while(i<n+1):
        i=i+1
        if (i%2==0):
            print(i,end=" ")
Number=int(input("Enter the number : "))
Even_Numbers(Number)

# Print Sum of First N Odd Numbers

def sum_odd_numbers(n):
 count=0
 sum=0
 num=1
 while count<n:
    sum=sum+num
    num=num+2
    count=count+1
 print(sum)
Number=int(input("Enter the number : "))
sum_odd_numbers(Number)

# Problem 4: Count the Occurrences of Digit '5'

def Count_digit(n,f):
    Store_Number=[]
    while n>0:
        digit=n%10
        Store_Number.append(digit)
        n=n//10
    print(Store_Number.count(f))

Number=int(input("Enter the number : "))
Find=int(input("Enter the number to count : "))
Count_digit(Number,Find)

# Problem 5: Find the Largest Digit in a Number

def Largest_Number(n):
    Numbers=[]
    while n>0:
        digit=n%10
        n=n//10
        Numbers.append(digit)
    print(max(Numbers))
Number=int(input("Enter the number : "))
Largest_Number(Number)

# Problem 6: Print Number in Words (Digits Only)

def Words_Digits(n):
    digit_words=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    digits=[]
    while n>0:
        last=n%10
        digits.append(last)
        n=n//10
    for digit in digits:
        print(digit_words[digit])
Number=int(input("Enter the number : "))
Words_Digits(Number)

# Problem 7: Product of Digits

def Product_Number(n):
    product=1
    while n>0:
        digit=n%10
        product=product*digit
        n=n//10
    print(product)
Product_Number(234)

# Problem 8: Number of Zeros in a Number

def Count_Zeros(n):
    Store=[]
    while n>0:
        digit=n%10
        Store.append(digit)
        n=n//10
    print(Store.count(0))
Number=int(input("Enter the number : "))
Count_Zeros(Number)

# Problem 9: Check Armstrong Number
def Armstrong_Number(n):
    nu=int(n)
    num=0
    while nu>0:
        length=len(n)
        digit=nu%10
        sum_all=digit**length
        num=num+sum_all
        nu=nu//10
    return num
Number=input("Enter the number : ")
call=Armstrong_Number(Number)
convert=int(Number)
if (convert==call):
    print("Yes")
else:
    print("No")

# Problem 10: Find GCD of Two Numbers (Using Subtraction Method)

def GCD(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print(GCD(20,8))