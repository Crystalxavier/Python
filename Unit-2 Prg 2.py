
# Practical 2: Student List and Marks

# List of student names
list1 = ["Amit", "Priya", "Rahul", "Neha", "Karan"]

# Nested list of student names and marks
list2 = [
    ["Amit", 75],
    ["Priya", 92],
    ["Rahul", 68],
    ["Neha", 85],
    ["Karan", 80]
]

# a) Search for a student
name = input("Enter student name to search: ")

if name in list1:
    print("Student found at index:", list1.index(name))
else:
    print("Student not found")

# b) Sort student names
list1.sort()
print("Ascending Order:", list1)
print("Descending Order:", sorted(list1, reverse=True))

# c) Add, insert and remove names
list1.append("Meera")
print("After adding:", list1)

list1.insert(2, "Riya")
print("After inserting:", list1)

remove_name = input("Enter name to remove: ")
if remove_name in list1:
    list1.remove(remove_name)
    print("After removing:", list1)
else:
    print("Name not found")

# d) Display all student records
print("\nStudent Records:")
for student in list2:
    print("Name:", student[0], "Marks:", student[1])

# e) Highest marks and average marks
highest = max(list2, key=lambda student: student[1])
total = sum(student[1] for student in list2)
average = total / len(list2)

print("Student with Highest Marks:", highest[0])
print("Highest Marks:", highest[1])
print("Average Marks:", average)

# f) Number of student records
print("Number of Student Records:", len(list2))
