def User_Turn_100(name,age):
    cal_age=100-age
    return (f"{name} turn 100 in {2025+cal_age}")
name=input("Enter the name : ")
age=int(input("Enter the age : "))
print(User_Turn_100(name,age))

def Swaping_NUmbers(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    return (f"num1:{num1},num2:{num2}")
num1=int(input("Enter the number1 : "))
num2=int(input("Enter the number2 : "))
print(Swaping_NUmbers(1,2))

def All_Arthamtics(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    power=num1**num2
    floar=num1//num2
    return (add,sub,mul,div,power,floar)
num1=int(input("Enter the num1 : "))
num2=int(input("Enter the num2 : "))
print(All_Arthamtics(num1,num2)) 

def Cal_Area_Peri(Length,Width):
    Area=Length*Width
    perimeter=2*(Length+Width)
    return (Area,perimeter)
print(Cal_Area_Peri(5,10)) 

def celcsius_to_fahrenheat(celsius):
    fahrenheat=(9/5)*celsius+32
    return fahrenheat
print(celcsius_to_fahrenheat(0)) 

def SI(amount,intrest,time):
    return (amount*intrest*time)/100
print(SI(1000,5,2)) 

def Sum_Of_Digits(number):
    sum=0
    while number>0:
        digit=number%10
        sum=sum+digit
        number=number//10
    return sum
print(Sum_Of_Digits(123)) 

def reverse_digit(number):
    sum=""
    while number>0:
        digit=number%10
        sum=sum+(str(digit))
        number=number//10
    return (int(sum))
print(reverse_digit(123)) 

def minutes_to_hour(Minutes):
    hours=Minutes//60
    minutes=Minutes%60
    return (f"{hours}:{minutes}")
print(minutes_to_hour(210)) 

def Sum_N_Numbers(number):
    sum=0
    for i in range(1,number+1):
        sum=sum+i
    return sum
print(Sum_N_Numbers(5)) 

def Cube_Square(number):
    cube=number**3
    square=number**2
    return (cube,square)
print(Cube_Square(3)) 
 