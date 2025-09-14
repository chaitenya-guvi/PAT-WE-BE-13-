# Indexing and Slicing in Python
# Indexing allows you to access individual characters in a string using their position (index).
# variablename[index]
# Indexing starts at 0 (the first character is at index 0).
# Negative indices can be used to access characters from the end (-1 is the last character).
# Example:
sample_str = "Hello, World!"
print("Sample string:", sample_str)
print("First character (index 0):", sample_str[0])
print("Last character (index -1):", sample_str[-1])

# More examples of indexing
print("Second character (index 1):", sample_str[1])
print("Fifth character (index 4):", sample_str[4])
print("Second to last character (index -2):", sample_str[-2])

# More examples of negative indexing
print("Third to last character (index -3):", sample_str[-3])
print("Fourth to last character (index -4):", sample_str[-4])
print("Fifth to last character (index -5):", sample_str[-5])


# Accessing characters using a loop
print("All characters in the string:")
for index in range(len(sample_str)):
    print(f"Index {index}: {sample_str[index]}")

# Accessing every character using negative indices
print("All characters using negative indices:")
for neg_index in range(-1, -len(sample_str)-1, -1):
    print(f"Index {neg_index}: {sample_str[neg_index]}")

# Negative indexing in a loop (showing index and character)
print("Characters and their negative indices:")
for offset in range(1, len(sample_str)+1):
    print(f"Index -{offset}: {sample_str[-offset]}")
