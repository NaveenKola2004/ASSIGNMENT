# Pattern 1: Stars in a Single Row

n=5
for i in range(n):
    print("*",end=" ")

# Pattern 2: Increasing Numbers in a Row

n=5
for i in range(1,n+1):
    print(i,end=" ")

for i in range(n,0,-1):
    print(i)


# Pattern 3: Alphabets in Single Row

n=5
for i in range(n):
    print(chr(65+i),end=" ")

n=5
for i in range(n,0,-1):
    print(chr(64+i),end=" ")

# Pattern 4: Square of Stars

n=3
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
# Reversed
n=3
for i in range(n,0,-1):
    for j in range(n):
        print("*",end=" ")
    print()
# Pattern 5: Increasing Numbers Row-wise


n=5
for i in range(1,n):
    for j in range(1,n):
        print(j,end=" ")
    print()


n=5
for i in range(1,n):
    for j in range(n-1,0,-1):
        print(j,end=" ")
    print()

# Pattern 6: Right-Angled Star Triangle

n=4

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=4

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# Pattern 7: Number Triangle (1 to n per row)

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Pattern 8: Alphabet Triangle

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

# Pattern 9: Repeating Alphabets in Triangle

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
    