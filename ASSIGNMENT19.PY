# 🧠 Medium-Level Logical Practice Problems

def Find_Missing_Number(number):
    Numbers=[1,2,3,4,5,6]
    for i in Numbers:
            if i not in number:
              return (f"The number {i} is missing")
print(Find_Missing_Number([1,2,4,5]))
print(Find_Missing_Number([2,3,1,6,5]))

# 2. 🔢 Count Digits with Even Frequency

def Count_Digit(number):
    Store=[]
    count=0
    while number>0:
        digit=number%10
        Store.append(digit)
        number=number//10
    for i in Store:
        if Store.count(i)>=2:
            count=count+1
    return count//2
number=int(input("enter the number : "))
print(Count_Digit(number))

# 3. 🧩 Find the First Non-Repeating Character

def First_Non_Repeacting_char(string):
    letters=[]
    for i in string:
        letters.append(i)
    for j in letters:
        if letters.count(j)<2:
            return j
string=input("Enter the string : ")
print(First_Non_Repeacting_char(string))

def First_Non_Repeacting_char(string):
    for i in string:
        if string.count(i)<2:
            return i
string=input("Enter the string : ")
print(First_Non_Repeacting_char(string))

# 4. 🔄 Rotate Array

def Rotate_Array(numbers,k):
    first=[]
    final=[]
    if k==2:
        for i in numbers[:len(numbers)-2]:
           first.append(i)
        for j in first:
            numbers.remove(j)
    final=numbers+first
    return final
print(Rotate_Array([1,2,3,4,5,6],2))

# 5. 🔠 Check Anagram

def Check_Anagram(string1,string2):
    for i in string1:
        if i in string2:
            print("Yes")
        else:
            print("no")
print(Check_Anagram("listen", "silent"))

def Check_Anagram(string1,string2):
    if sorted(string1)==sorted(string2): # Logic checked using AI 
        return "yes"
    else:
        return "no"
print(Check_Anagram("listen", "silent"))

# 6. 📏 Longest Word in Sentence
def Longest_Word(sentance):
    word=sentance.split()
    longest=max(word, key=len)
    return longest
print(Longest_Word("Python is fun and powerful"))

# 7. 💡 Convert Integer to Binary (Without Built-in Function)

def Binary_convert(n):
    binary=""
    while n>0:
        digit=n%2
        binary=str(digit)+binary
        n=n//2
    return binary
number=int(input("Enter the number : "))
print(Binary_convert(number))

# 8. 🔂 Sum of Digits Until Single Digit

def Sum_digit(n):
    sum1=0
    sum2=0
    final=0
    while n>0:
        digit=n%10
        sum1=sum1+digit
        n=n//10
    while sum1>0:
        digit=sum1%10
        sum2=sum2+digit
        sum1=sum1//10
    while sum2>0:
        digit=sum2%10
        final=final+digit
        sum2=sum2//10
    return final

print(Sum_digit(98753))

# 9. 🔄 Count and Print Even and Odd Numbers Separately

def Seperate_Numbers(numbers):
    even=[]
    odd=[]
    for i in numbers:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return (f"Even : {even} \n Odd : {odd}")
print(Seperate_Numbers([1,2,3,4,5,6]))

# 10. 📃 Print Numbers Divisible by 3 and 5 but Not Both

def Numbers_divide_5_3(n):
    store=[]
    for i in range(1,n+1):
        if (i%3==0 and i%5!=0) or (i%5==0 and i%3!=0):
            store.append(i)
    return store
print(Numbers_divide_5_3(15))
# 11. 🔢 Print Prime Numbers in a Range

def prime_numbers(n):
    primes=[]
    for i in range(2,n+1):
        prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=False
                break
        if prime:
            primes.append(i)
    print(primes)
prime_numbers(10)        

def prime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True
number=int(input("Enter the number : "))
if prime(number):
    print("prime")
else:
    print("not prime")