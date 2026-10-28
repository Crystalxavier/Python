
# Practical 4: String Operations

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# a) Display strings and their lengths
print("First String:", str1)
print("Second String:", str2)
print("Length of First String:", len(str1))
print("Length of Second String:", len(str2))

# b) Positive and negative indexing
if len(str1) > 0:
    print("First Character:", str1[0])
    print("Last Character:", str1[-1])
else:
    print("First string is empty")

# c) Slicing
print("Substring of First String:", str1[0:3])
print("Substring of Second String:", str2[0:3])

# d) Repetition and concatenation
print("Repeated First String:", str1 * 2)
print("Concatenated Strings:", str1 + str2)

# e) Membership operators
character = input("Enter character or substring to search: ")
print("Using in:", character in str1)
print("Using not in:", character not in str1)

# f) String comparisons
print("Equal (==):", str1 == str2)
print("Not Equal (!=):", str1 != str2)
print("Less Than (<):", str1 < str2)
print("Greater Than (>):", str1 > str2)

# g) Uppercase and lowercase
print("First String in Uppercase:", str1.upper())
print("First String in Lowercase:", str1.lower())
print("Second String in Uppercase:", str2.upper())
print("Second String in Lowercase:", str2.lower())
