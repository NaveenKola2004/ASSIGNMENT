# TWO SUM

def Two_Sum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return [i,j]
print(Two_Sum([3,2,4],6))

