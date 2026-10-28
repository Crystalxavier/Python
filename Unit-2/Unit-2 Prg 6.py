
# Practical 6: Array Operations

import array

numbers = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])

# a) Display array, indexing and slicing
print("Original Array:", numbers)
print("Element at index 2:", numbers[2])
print("Last Element:", numbers[-1])
print("Slicing:", numbers[2:6])

# b) Insert an element at a specified position
position = int(input("Enter position to insert (0-8): "))
if 0 <= position <= len(numbers):
    value = int(input("Enter value to insert: "))
    numbers.insert(position, value)
    print("After insertion:", numbers)
else:
    print("Invalid position")

# c) Remove a specified element and last element
value = int(input("Enter element to remove: "))
if value in numbers:
    numbers.remove(value)
    print("After remove():", numbers)
else:
    print("Element not found")

if len(numbers) > 0:
    removed = numbers.pop()
    print("Popped Element:", removed)
    print("After pop():", numbers)

# d) Search for an element
search_value = int(input("Enter element to search: "))
if search_value in numbers:
    print("Element found at index:", numbers.index(search_value))
else:
    print("Element not found")

# e) Membership operators
element = int(input("Enter element to check membership: "))
print("Using in:", element in numbers)
print("Using not in:", element not in numbers)

# f) Maximum, minimum and length
if len(numbers) > 0:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
print("Length:", len(numbers))

# g) Reverse the array
numbers.reverse()
print("Reversed Array:", numbers)
