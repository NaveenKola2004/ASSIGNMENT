# Printing the binay values of the numbers
n=10
a=[]
while n>0:
    bite=n%2
    a.append(bite)
    n=n//2
a.reverse()
print(a)

# odd or even using function

def find_odd_even(n):
    if (n%2==0):
        return "EVEN"
    else:
        return "ODD"
print(find_odd_even(10))

# Find NEGITIVE AND ZERO AND POSITIVE

def Find_neg_Zero_pos(n):
    if(n<0):
        return "NEG"
    elif(n>0):
        return "POS"
    else:
        return "ZERO"
print(Find_neg_Zero_pos(9))

# GRATER 2 numbers
def FIND_largest_two_numbers(num1,num2):
    if (num1>num2):
        return num1,"is grater numbers"
    else:
        return num2,"is grater number"
print(FIND_largest_two_numbers(8,12))

def Grade_generator(mark):
    if (mark>90):
        return "A"
    elif(mark>80 and mark<89):
        return "B"
    elif(mark>70 and mark<79):
        return "C"
    elif(mark>60 and mark<69):
        return "D"
    else:
        return "F"
print(Grade_generator(55))