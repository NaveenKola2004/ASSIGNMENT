def Subtraction_Numbers(a,b):
    if a==0 or b==0:
        if a==0:
            print("Please change the value of 'a' you entered ' 0 '")
        else:
            print("Please change the value of 'b' you entered ' 0 '")
        return None
    print(f"{a} - {b} = {a-b}")
