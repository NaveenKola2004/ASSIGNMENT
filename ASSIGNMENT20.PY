# Problem 1: Alternating Sum

def Alternating_Sum(numbers):
    total_sum=0
    for i,j in enumerate(numbers):
        if i%2==0:
            total_sum=total_sum+j
        else:
            total_sum=total_sum-j
    return total_sum
print(Alternating_Sum([5,3,8,1,4]))

# Problem 2: Consecutive Pairs

def consecutive_pairs(n):
    n=()
    for i in n:
        print(i)
consecutive_pairs([1,2,3,4,5,6])
