#1. Arithmetic Operators

num1=int  (input())
num2=int  (input())


result=["Addition : ",num1+num2,
   "Subtraction : ",num1-num2, 
   "multiplication : ",num1*num2, 
   "division : ",num1/num2, 
   "flooe division : ",num1//num2, 
   "modulus : ",num1%num2, 
   "exponentiation : ",num1**num2 
]
print(result)

#2. Comparison Operators

num1=int(input())
num2=int(input())
result= ["Equal to : ",num1==num2,
 "Not equal to ",num1!=num2,
 "Graterthen ",num1>num2,
 "Lesserthen : ",num1<num2,
 "Greterthen and equal : ",num1>=num2,
 "Lesserthen and equal : ",num1<=num2
 ]

print(result)

# 3. Logical Operators

a=True
b=False
result=[
        "and :",a and b ,
        "or : ",a or b,
        "not a : ",not a,
        "not b ",not b
        ]
print(result)

# 4. Identity Operators

a=[1,2,3]
b=[1,2,3]
result=[
    "a is b -> ",a is b,
    "a is not b -> ",a is not b
]
print(result)

x= 42
y=42
result2=[
    "x is y -> ",x is y,
    "x is not y -> ",x is not y
]
print(result2)

# 5. Membership Operators

string="Python"
char='y'
result=[
    "y in python -> ",char in string,
    "y not in python -> ",char not in string 
]
print(result)

string2="Hello"
char2="z"
result2=[
    "z in hello -> ",char2 in string2,
    "z not in hello ->",char2 not in string2 
]
print(result2)

# 6. Membership in a List

fruits=["banana","apple","cherry"]
needed_fruit="banana"
result=[
    "banana in fruits ->",needed_fruit in fruits,
    "banana not in fruits -> ",needed_fruit not in fruits
]
print(result)

numbers=[1,2,3,4]
number=5
result2=[
    "5 in numbers -> ",number in numbers,
    "5 not in numbers -> ",number not in numbers
]
print(result2)

# 7. Arithmetic Puzzle

a=5
b=8
result =[a *(b%a),(a+b) / (b-a),(a**2) + (b**3)]
print(result)

#8. Complex Comparison

x=12
y=8
z=15
result=[
    x>y and x>z,
    y<x and y<z,
    (x is not y) and  (x is not z) and (y is not z)
]
print(result)

#9. Logical Operations Challenge

A=True
B=False
C=True

result = [
    A is not B or C,
    not (A or B) and C
]
print(result)

#10. Identity and Membership Check

L=[3,7,2,7]
X=7
largest=max(L)
L.sort()
result= [
    X in L and X is largest,
    X not in L or X > L[0] and X > L[1] and X > L[2] and X > L[3],
    (L[0] == L[1]) or (L[0] == L[2]) or (L[0] == L[3]) or (L[1] ==L[2]) or (L[1]==L[3]) or (L[2] ==L[3]) # we are checking minimum elements in list
]
print(result)

#11. Advanced Membership Testing

s="racecar"
sub="car"
re=sub[::-1]
result= [
    sub in s,
    sub in s,
    s.startswith(sub) and s.endswith(sub)
]
print(result)
