from Inventory.show_stock import *
def Create_order(type):
    while True:
     if type=="tiffen":
        print(tiffen)
        order=input("Enter the food item : ")
        if order in tiffen.values():
          print("Order conformed")
        else:
            print("Item not avilable")
     elif type=="lunch":
        print(lunch)
        order=input("Enter the food item : ")
        if order in lunch.values():
          print("Order conformed")
        else:
            print("Item not avilable")
     elif type=="dinner":
        print(dinner)
        order=input("Enter the food item : ")
        if order in dinner.values():
          print("Order conformed")
        else:
            print("Item not avilable")

     next_order = input("\nDo you want to order again? (yes/no): ").lower()

     if next_order in ["no"]:
          print("ok,sir thank you Have a great day!")
          break