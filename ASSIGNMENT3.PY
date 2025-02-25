#1. Name Tag Formatter
value=input()
print(value.title())

#2. Document Title Formatter
value=input()
print(value.capitalize())

#3. Secret Code Generator

value=input()
print(value.swapcase())

#4. Loudspeaker Announcement

value=input()
print(value.upper())

#5. Whisper Mode
value=input()
print(value.lower())

#6. Censorship System

value=input()
print(value.replace('bad','***'))

#7. Auto-Correct System

value=input()
print(value.replace('r','are',1).replace('u','you',1))

#8. Space Trimmer

value=input()
print(value.strip())

#9. Check If Input Is Numeric

value=input()
print(value.isdigit())

#10. Check If Input Contains Only Alphabets

value=input()
print(value.isalpha())

#11. String Formatting: Dynamic Greeting Message

value=input()
print(f"Hello,{value}! Welcome to our platform.")

#12. String Formatting: Report Card Generator

value=input()
marks=float(input())
print(f"Student:{value}|Score:{marks:.2f}%")

#13. String Formatting: Product Price Tag
product=input()
price=float(input())
print(f"Product:{product}|Price:₹{round(price,2)}%")