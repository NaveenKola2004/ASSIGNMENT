# Printing the binay values of the numbers
n=10
a=[]
while n>0:
    bite=n%2
    a.append(bite)
    n=n//2
a.reverse()
print(a)

