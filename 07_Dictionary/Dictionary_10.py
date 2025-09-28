# The fromkeys() method in Python dictionaries
# -------------------------------------------
# The fromkeys() method creates a new dictionary with specified keys and a single value for all keys.
# Syntax: dict.fromkeys(keys, value)
# used to create a new dictionary with default values
# If value is not provided, the default is None.

# Example 1: Basic usage with a list of keys
keys = ["a", "b", "c"]
d1 = {}.fromkeys(keys)
print("Fromkeys with default value:", d1)  # Output: {'a': None, 'b': None, 'c': None}

# Example 2: Basic usage with a tuple of keys and a custom value
tuple_keys = (1, 2, 3)
d2 = dict.fromkeys(tuple_keys, 0)
print("Fromkeys with custom value:", d2)  # Output: {1: 0, 2: 0, 3: 0}

# Example 3: Using a string as keys (each character becomes a key)
chars = "xyz"
d3 = dict.fromkeys(chars, True)
print("Fromkeys with string:", d3)  # Output: {'x': True, 'y': True, 'z': True}

# Example 4: Using a set as keys
key_set = {"apple", "banana"}
d4 = dict.fromkeys(key_set, 1)
print("Fromkeys with set:", d4)  # Output: {'apple': 1, 'banana': 1}

# Intermediate Example 1: Creating a dictionary for default settings
settings_keys = ["theme", "volume", "language"]
default_settings = dict.fromkeys(settings_keys, "default")
print("Default settings:", default_settings)  # Output: {'theme': 'default', 'volume': 'default', 'language': 'default'}

# Intermediate Example 2: Initializing a dictionary for counting (all counts start at 0)
count_keys = ["red", "green", "blue"]
color_counts = dict.fromkeys(count_keys, 0)
print("Color counts:", color_counts)  # Output: {'red': 0, 'green': 0, 'blue': 0}

#  calling the fromkeys method on an existing dictionary will not impact the old dictionary
existing_dict = dict(name = 1 , age = True)
example_keys = ["color", "height"]
print(f"original dict : {existing_dict}")
existing_dict.fromkeys(example_keys,0)
print(f"updated dictionary {existing_dict}")


# Note: If the value is a mutable object (like a list), all keys will reference the same object.

# Summary:
# - fromkeys() creates a new dictionary with specified keys and a single shared value.
# - Useful for initializing dictionaries with default values.
# - Be careful with mutable default values (all keys share the same object).

