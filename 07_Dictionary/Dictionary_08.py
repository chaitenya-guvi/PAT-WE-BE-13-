# The clear() method in Python dictionaries
# ----------------------------------------
# The clear() method removes all key-value pairs from a dictionary, making it empty.
# It is useful when you want to reset a dictionary or reuse it for new data.

# Example 1: Basic usage
student = {"name": "Alice", "age": 20, "grade": "A"}
student.clear()
print("After clear:", student)  # Output: {}


# Example 2: Clear a dictionary after processing
word_count = {"the": 3, "cat": 2, "dog": 1}
for word, count in word_count.items():
    print(f"{word}: {count}")
word_count.clear()
print("Word count after clear:", word_count)  # Output: {}

# Example 3: Resetting a configuration dictionary
config = {"theme": "dark", "volume": 80, "language": "en"}
print("Before clear:", config)
config.clear()
print("After clear:", config)  # Output: {}

# Summary:
# - clear() removes all items from a dictionary, leaving it empty.
# - It modifies the original dictionary in place and does not return a new dictionary.
# - Useful for resetting dictionaries in programs, such as after processing or reconfiguration.

