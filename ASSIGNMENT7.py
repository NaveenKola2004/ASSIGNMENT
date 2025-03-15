#1. Check if a Number is Even or Odd

num=int(input("Enter the number : "))
if (num%2==0):
    print(num,"is even number ")
else:
    print(num,"is odd number")

#2. Check Positive, Negative, or Zero

num=int(input("Enter the number :"))

if(num<0):
    print(num,"is negitive number")
elif(num>0):
    print(num,"is positive number")
else:
    print("Zero")

#3. Find the Largest of Two Numbers

num1=int(input("Enter the number : "))
num2=int(input("Enter the another number :"))
if(num1>num2):
    print(num1,"IS gratest number")
else:
    if(num2>num1):
        print(num2,"is gratest number")
    else:
        print("you entered both zeros")

#4. Check if a Year is a Leap Year

year=int(input("Enter the year : "))

if(year%4==0 and year % 100 !=0):
    print("is leap year")
else:
    print("is not leap year")

#5. Grade Calculator

marks=int(input("Enter your marks : "))

if(marks >= 90 and marks <100):
    print("A")
elif(marks >= 80 and marks <89 ):
    print("B")
elif(marks >=70 and marks <79):
    print("C")
elif(marks >=60 and marks <69):
    print("D")
else:
    print("F")

#6. Find the Smallest of Three Numbers

num1=int(input("Enter the First number  : "))
num2=int(input("Enter the Second number :"))
num3=int(input("Enter the Third number  :"))

if(num1<num2):
    if(num1<num3):
        print(num1)
    else:
        print(num3)
else:
    if(num2<num3):
        print(num2)
    else:
        print(num3)

#7. Check if a Character is a Vowel or Consonant

character=input("Enter the character : ")

if (character == "a" or character=="e" or character=="i" or character=="o" or character=="u"):
    print("vowel")
else:
    print("Consonant")

#8. Ticket Pricing Based on Age

age=int(input("Enter your age : "))

if(age <= 5):
        print("Free")
else:
    if(age > 5 and age <=18):
        print("100")
    else:
         print("200")
    
#9. Check if a Triangle is Valid

a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))

if(a+b >c and a+c >b and b+c >a):
    print("valid triangle")
else:
    print("invalid triangle")

#10. Check Divisibility by 5 and 11

num=int(input("Enter the number :"))

if(num%5==0 and num%11==0):
    print("Divisible by both")
else:
    print("not divisible by both")