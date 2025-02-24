#1. Print User Input

name=input()
print("Hello",name,sep=",")

#2. Convert Integer to Float

num=int(input())
change_num=float(num)
print(change_num)

#3. Extract First and Last Character of a String

value="PYTHON"

print(value[0],value[5])

print(value[0:6:5])

#4. Slice First Three Characters of a String

value="HELLO"
print(value[0:3])

#5. Extract Last Three Characters of a String

value="Programming"
print(value[-3:])
print(value[8:11])

#6. Extract a Substring from Index 2 to 5

value="Programming"
print(value[2:6])

#7. Extract Every Second Character from a String

Value="abcdef"
print(Value[1:6:2])

#8. Reverse a String Using Slicing

value="PYTHON"
print(value[::-1])

#9. Extract First Half of a String

value="pythonista"
print(value[0:6])

#10. Extract Last Half of a String

Value="pythonista"
print(Value[-5:])
print(Value[5:11])

#11. Convert Float to Integer

num=float(input())
change_num=int(num)
print(change_num)

#12. Find Index of a Character in a String

value="python"
print(value.index('p'))