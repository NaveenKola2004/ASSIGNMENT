# 1. Find the First Repeating Number
num=[1,2,3,4,434,2332,23,2,123,3]

repeat=set()

for i in num:
    if i in repeat:
        print(i)
        break
    repeat.add(i)

# 2. Find the First Non-Repeating Character in a String
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

# 