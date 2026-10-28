
# Practical 1: List Operations

numbers = list(range(1, 11))

# a) Display list, indexing and slicing
print("Original List:", numbers)
print("Positive Indexing (index 2):", numbers[2])
print("Negative Indexing (index -1):", numbers[-1])
print("Slicing (index 2 to 6):", numbers[2:7])

# b) Update an element at a specified index
index = int(input("Enter index to update (0-9): "))
if 0 <= index < len(numbers):
    value = int(input("Enter new value: "))
    numbers[index] = value
    print("Updated List:", numbers)
else:
    print("Invalid index")

# c) Concatenation and repetition
print("Concatenation:", numbers + [11, 12])
print("Repetition:", numbers * 2)

# d) Membership operators
num = int(input("Enter a number to search: "))
print("Using in:", num in numbers)
print("Using not in:", num not in numbers)

# e) List methods
numbers.append(20)
print("After append:", numbers)

numbers.insert(2, 15)
print("After insert:", numbers)

numbers.remove(15)
print("After remove:", numbers)

removed = numbers.pop()
print("Popped Element:", removed)
print("After pop:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Count of 5:", numbers.count(5))

# f) Sorting
numbers.sort()
print("Ascending Order:", numbers)
print("Descending Order:", sorted(numbers, reverse=True))

# g) Aliasing and cloning
alias = numbers
clone = numbers.copy()

alias[0] = 100
print("Original after modifying alias:", numbers)
print("Alias:", alias)
print("Clone (independent copy):", clone)

# h) Maximum, minimum and length
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Length:", len(numbers))
