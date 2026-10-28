# Write a program to create a menu with the following options:
# Accept user input and perform the operations. Use function with arguments
# To perform addition
# To perform subtraction
# To perform multiplication
# To perform division

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b
print("------------Menu----------")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
choice = int(input("Please select the choice (1-4): "))
num1 = int(input("Please enter Num1 : "))
num2 = int(input("Please enter Num2 : "))

if choice==1:
    print("Addition = ",addition(num1,num2))
elif choice==2:
    print("Subtraction = ",subtraction(num1,num2))
elif choice==3:
    print("Multiplication = ",multiplication(num1,num2))
elif choice==4:
    if (num2 != 0):
        print("Division =", division(num1, num2))
    else:
        print("Can not divide by zero")
else:
    print("Invalid Choice")
