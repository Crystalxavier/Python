# Create a tuple and perform the following methods: Add items(), Check item
# in a tuple(), len(), Access items()

# create a tuple
languages = ("C++","Java","PHP")

# Add item in tuple
languages = ("React",) + languages + ("Java",)
print("After adding elements to tuple :",languages)

# check the item is available in tuple
if "React" in languages:
    print("React is in the tuple")
else:
    print("React is not in the language tuple")

# check the length of the tuple
print("Length of the tuple :",len(languages))

# Access the elements of the tuple
print("First item of the tuple :",languages[0])
print("First item of the tuple :",languages[1])
print("Last item of the tuple :",languages[-1])
