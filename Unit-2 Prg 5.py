
# Practical 5: String Methods

sentence = input("Enter a sentence: ")

# Remove leading and trailing spaces
print("Using lstrip():", sentence.lstrip())
print("Using rstrip():", sentence.rstrip())
print("Using strip():", sentence.strip())

# Use the cleaned sentence for further operations
sentence = sentence.strip()

# a) Search using find() and index()
substring = input("Enter substring to search: ")

position = sentence.find(substring)
print("Position using find():", position)

if position != -1:
    print("Position using index():", sentence.index(substring))
else:
    print("Substring not found; index() cannot locate it.")

# b) Count occurrences of a word
word = input("Enter word to count: ")
print("Occurrences:", sentence.count(word))

# c) Replace a word or character
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement: ")
print("After replacement:", sentence.replace(old_word, new_word))

# d) Split and join
words = sentence.split()
print("Words:", words)
print("Joined Sentence:", "-".join(words))

# e) Demonstrate string immutability
try:
    sentence[0] = "A"
except TypeError:
    print("String cannot be modified using indexing.")
    print("Strings are immutable in Python.")

# f) Sort words alphabetically
sorted_words = sorted(words, key=str.lower)
print("Alphabetically Sorted Words:", sorted_words)
