# Problem 1: Alternating Sum

def Alternating_Sum(n):
   even=0
   odd=0
   for i in range(len(n)):
      if (i%2==0):
            even=even+n[i]
      else:
            odd=odd+n[i]
   return even-odd
print(Alternating_Sum([5,3,8,1,4]))

#Problem 2: Consecutive Pairs

def Consecutive_Pairs(n):
   pairs=[]
   for i in range(len(n)-1):
      a=n[i]
      b=n[i+1]
      if (b>a):
         pairs.append((a,b))
   print(pairs)
Consecutive_Pairs([1,2,3,4,5,6])

# Peak Finder

def Peak_Finder(n):
   count=0
   for i in range(len(n)-2):
        a=n[i]
        b=n[i+1]
        c=n[i+2]
        if (b>a and b>c):
            count=count+1
   return count
print(Peak_Finder([1,3,2,5,3,9,8]))

#  Running Sum with Threshold


