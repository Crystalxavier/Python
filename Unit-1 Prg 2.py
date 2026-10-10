# Write a menu driven python program which performs the following:
# (Implement using if-else)
# a. Find area of circle ( 3.14 * r * r)
# b. Find area of triangle (0.5 * base * height)
# c. Find area of square and rectangle (side * side)(length * breath)
# d. Find Simple Interest

print("----- MENU -----")
print("1. Area of Circle")
print("2. Area of Triangle")
print("3. Area of Square")
print("4. Area of Rectangle")
print("5. Simple Interest")
choice = int(input("Enter your choice: "))
if choice == 1:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)
elif choice == 2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)
elif choice == 3:
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square =", area)
elif choice == 4:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)
elif choice == 5:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))
    si = (principal * rate * time) / 100
    print("Simple Interest =", si)
else:
    print("Invalid choice")