def User_Input(name):
    return (f"Hello,{name}")
name=input("Enter your name : ")
print(User_Input(name))

def Int_To_Float(number):
    return float(number)
number=int(input("Enter the number : "))
print(Int_To_Float(number))

def Extract_1_2(string):
    return (string[0:len(string):len(string)-1])
word=input("Enter the word : ")
print(Extract_1_2(word))

def First_3(string):
    return (string[0:3])
word=input("Enter the word : ")
print(First_3(word))

def Second_char(string):
    return (string[1:len(string):2])
word=input("enter the number : ")
print(Second_char(word))

def Reverse(string):
    word=""
    for i in string:
        word=i+word
    return word
word=input("Enter the string : ")
print(Reverse(word))

def First_Half(string):
    le=round(len(string)/2)
    return(string[0:le])
word=input("Enter the word : ")
print(First_Half(word))

def Second_Half(string):
    le=round(len(string)/2)
    return (string[le:len(string)])
word=input("Enter the word : ")
print(Second_Half(word))