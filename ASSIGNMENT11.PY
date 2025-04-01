#1. Sum of First N Natural Numbers

num=int(input("Enter the number : "))
sum=0
for i in range (1,num+1):
    sum=sum+i
print(sum)

#2. Factorial of a Number
num=int(input("Enter the number : "))

fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
# 3. Print Multiplication Table

num=int(input("Enter the number  : "))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

#4. Reverse a Given String
string=input("Enter the word : ")

rev=" "

for i in string:
    rev=i+rev
print(rev)

# 5. Count Even and Odd Numbers in a List
list=[1,2,3,4,5,6,7,8,9,10]

even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
for i in list:
    if i%2!=0:
        odd.append(i)
print("Even count:",len(even))
print("Odd count:",len(odd))
# 6. Print Fibonacci Series

num=int(input("Enter the number : "))

a,b=0,1

print(a,b,end=" ")

for i in range(1,num-1):

    c=a+b
    print(c,end=" ")
    a,b=b,c
# 7. Find the Largest Number in a List
list=[1,2,3,4,444,87,687,909]

lar=list[0]

for i in list:
    if i>lar:
        lar=i
print(lar)
# 8. Count the Number of Vowels in a String
word=input("Enter the word : ")

word=word.lower()
vowels="aeiou"
count=0
for i in word:
    if vowels in word:
        count=count+1
print(count)

# 9. Print a Pattern (Right-Angled Triangle)
num=int(input("Enter the number  lines : "))

for i in range(1,num+1):
    print("*"*i)

# 10. Remove Duplicates from a List
list=[1,2,23,1,1,1,2,3,4,56,7,8,97]

sample=[]

for i in list:
    if i not in sample:
        sample.append(i)
print(sample)