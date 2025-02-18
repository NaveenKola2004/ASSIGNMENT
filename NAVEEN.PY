# 1. Calculate the Year When the User Turns 100

Name=input("Enter your name  : ")
Age=int(input("Enter your age : "))
cal=(100-Age)
year=2025+cal
print(Name,"is turn 100 in ",year)

#2. Swap Two Numbers Using Arithmetic Operations

num1=float(input("Enter the number : "))
num2=float(input("Enter the number : "))
temp=num1
num1=num2
num2=temp
print("num1 : ",num1,"   num2 : ",num2)

#3. Perform All Arithmetic Operations

num1=int(input("Enter the number number : "))
num2=int(input("Enter the another number : "))
print("Addition :        ",num1+num2)
print("Subtraction :     ",num1-num2)
print("Multiplication :  ",num1*num2)
print("Division :        ",num1/num2)
print("Floredivision :   ",num1//num2)
print("Modulation :      ",num1%num2)

#4. Calculate Area and Perimeter of a Rectangle

length=int(input("Enter the length : "))
width=int(input("Enter the width  : "))
Area=length*width
perimeter=2*(length+width)
print("Area : ",Area,"\nPerimeter : ",perimeter)

#5. Convert Celsius to Fahrenheit

Temperature=float(input("Enter Temperature : "))
Fahrenheit=(9/5)*Temperature+32
print(Fahrenheit)

#6. Calculate Simple Interest

Amount=int(input("Enter the Total amount : "))
RATE_intrest=int(input("Enter the intrest : "))
Time=int(input("Enter the no.of Years : "))
simple_intreat=(Amount*RATE_intrest*Time)/100
print(simple_intreat)

#7. Find Sum of Digits of a 3-Digit Number


#8. Reverse a 3-Digit Number

num=int(input("Enter the number : "))
convert=str(num)
reverse=convert[::-1]
print(reverse)


#9. Convert Total Minutes to Hours and Minutes

time=int(input("Enter the time in minutes : "))
convert=time/60
print(convert)

#10. Sum of First N Natural Numbers

number=int(input("Enter the number : "))
sum=(number*(number+1)//2)
print(sum)

#11. Find Square and Cube of a Number

number=int(input("Enter the Number : "))
square=number**2
cube=number**3
print("SQUARE : ",square,"\nCUBE : ",cube)
