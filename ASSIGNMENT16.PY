# 1. Flipped Right Angled Triangle

# Using '*'
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

# Using Numbers

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(k+1,end=" ")
    print()

# Using Alphabets

n=3
for i in range(1,n+1):
    for j in range(n-i):
          print(" ",end=" ")
    for k in range(i):
        print(chr(65+k),end=" ")
    print()

# 2. Reversed Flipped Right Angled Triangle

# Using "*"

n=4

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

#Using Numbers
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(i):
        print(k+1,end=" ")
    print()
# Using Alphabets

n=3

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(chr(65+k),end=" ")
    print()

# 3. Pyramid

#Using '*'
n=4

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

#Using Numbers

n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(k+1,end=" ")
    print()

#Using Alphabets

n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(chr(65+k),end=" ")
    print()

# 4. Reverse Pyramid
#Using '*'
n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

#Using Numbers

n=3

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(k+1,end=" ")
    print()

# using Alphabets

n=3

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(chr(65+k),end=" ")
    print()

# 5. Diamond

#Using '*'
n=3
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

#Using Numbers

n=2
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(k+1,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(k+1)
    print()

#Using Alphabets

n=2
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(chr(65+j),end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(chr(65+k),end=" ")
    print()

# 6. Hollow Square

n=5
for i in range(n):
    for k in range(n):
        if i==0 or i==n-1 or k==0 or k==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Using Numbers

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

#Using Alphabets

n=3
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(chr(65+j),end=" ")
        else:
            print(" ",end=" ")
    print()

# 7. Hollow Right Angled Triangle

# Using '*'
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==i or j==1 or i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Using Numbers

n=4 
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==i or i==n or j==1 :
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

#Using Alphabets

n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or j==i:
            print(chr(64+j),end=" ")
        else:
            print(" ",end=" ")
    print()

# 8 Reversed Hollow Right Angled Triangle
#USing '*'
n=5
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==i or j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Using Numbers

n=4
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

#USing Alphabets

n=4
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(chr(64+j),end=" ")
        else:
            print(" ",end=" ")
    print()

