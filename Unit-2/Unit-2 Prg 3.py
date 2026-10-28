
# Practical 3: Tuple Operations

numbers = (10, 20, 30, 20, 40, 50, 60, 30, 70, 80)

# a) Display tuple, indexing and slicing
print("Original Tuple:", numbers)
print("Positive Indexing (index 2):", numbers[2])
print("Negative Indexing (index -1):", numbers[-1])
print("Slicing:", numbers[2:6])

# b) Concatenation and repetition
print("Concatenation:", numbers + (90, 100))
print("Repetition:", numbers * 2)

# c) Membership operators
element = int(input("Enter element to check: "))
print("Using in:", element in numbers)
print("Using not in:", element not in numbers)

# d) Maximum, minimum and length
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Length:", len(numbers))

# e) Count occurrences
value = int(input("Enter value to count: "))
print("Occurrences:", numbers.count(value))

# f) Search using index()
search_value = int(input("Enter value to search: "))

if search_value in numbers:
    print("Element found at index:", numbers.index(search_value))
else:
    print("Element not found in tuple")
