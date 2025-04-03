# 1. Find the First Repeating Number
num=[1,2,3,4,434,2332,23,2,123,3]

repeat=set()

for i in num:
    if i in repeat:
        print(i)
        break
    repeat.add(i)

# 2. Find the First Non-Repeating Character in a String
valu="swiss"
unq=set()
rep=set()

for i in valu:
    if i in rep:
        unq.add(i)
    else:
        rep.add(i)
for j in valu:
    if j not in unq:
        print(j)
        break
else:
    print("no repeting value")
# 3. Find the Largest Odd Number in a List
numbers = [10, 34,  12]

odd=[]
for i in numbers:
    if i%2!=0:
        odd.append(i)
if (odd):
    print(max(odd))
else:
    print("NO ODD NUMBER")

# 4. Print Numbers That Are Multiples of Both 3 and 5
num=int(input("Enter the  number :  "))

for i in range(1,num+1):
    if i % 5==0 and i % 3==0:
        print(i,end=" ")
# 5. Reverse Words in a Sentence (Keep Order)
sen=input("Enter the sentence : ")
for i in sen.split():
    print(i[::-1],end=" ")

# 6. Check if a Number is a Palindrome

word=input("Entere the word to check palindrome or not : ")

for i in word.split():
    if i==word[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")
#   7. Count Consecutive Ones in a Binary String

# 8. Print a Right-Angled Triangle Pattern with Odd Numbers
n=1
row =int(input("Enter the number of rows : "))

for i in range(1,row+1):
    for j in range(i):
        print(n,end=" ")
        n+=2
    print()

#   9. Find the Most Frequent Number in a List
# 10. Print Numbers with Distinct Digits
