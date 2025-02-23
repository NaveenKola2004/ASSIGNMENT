# 1. Calculate the Year When the User Turns 100

Name=input()
Age=int(input())
cal=(100-Age)
year=2025+cal
print(Name,"was turn 100 in ",year)

#2. Swap Two Numbers Using Arithmetic Operations

num1=float(input())
num2=float(input())
num1,num2=num2,num1
print(num1,num2)

#3. Perform All Arithmetic Operations

num1=int(input())
num2=int(input())
print("Addition :        ",num1+num2)
print("Subtraction :     ",num1-num2)
print("Multiplication :  ",num1*num2)
print("Division :        ",num1/num2)
print("Floredivision :   ",num1//num2)
print("Modulation :      ",num1%num2)

#4. Calculate Area and Perimeter of a Rectangle

length=int(input())
width=int(input())
Area=length*width
perimeter=2*(length+width)
print("Area : ",Area,"\nPerimeter : ",perimeter)

#5. Convert Celsius to Fahrenheit

Temperature=float(input())
Fahrenheit=(9/5)*Temperature+32
print(Fahrenheit)

#6. Calculate Simple Interest

Amount=int(input())
RATE_intrest=int(input())
Time=int(input())
simple_intreat=(Amount*RATE_intrest*Time)/100
print(simple_intreat)

#7. Find Sum of Digits of a 3-Digit Number

num=123
last=num%10
rem=num//10
a=last
last2=rem%10
rem2=rem//10
b=last2
last3=rem2%10
rem3=rem2//10
c=last3
print(a+b+c)
print(a*b*c)
#8. Reverse a 3-Digit Number

num=int(input())
last=num%10
a=last
rem=num//10
last=rem%10
b=last
rem=rem//10
last=rem%10
c=last
rem=rem//10
print(a,b,c)
print(a*100+b*10+c*1)



#9. Convert Total Minutes to Hours and Minutes

time=int(input())
convert=time/60
print(convert)

#10. Sum of First N Natural Numbers

number=int(input())
sum=(number*(number+1)//2)
print(sum)

#11. Find Square and Cube of a Number

number=int(input())
square=number**2
cube=number**3
print("SQUARE : ",square,"\nCUBE : ",cube)
