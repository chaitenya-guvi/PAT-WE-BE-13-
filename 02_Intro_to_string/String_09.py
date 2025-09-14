# Slicing allows you to extract a substring from a string using a range of indices.
# The syntax is string[start:end], where 'start' is inclusive and 'end' is exclusive.
# You can also specify a step: string[start:end:step]
# Example:

sample_str = "abcdefghijklmnopqrstuvwxyz"
print("Sample string:", sample_str)

hello_string = "Hello, World!"
print("Hello string:", hello_string)

for(index, character) in enumerate(hello_string):
    print(f"Index {index}: {character}")

print(hello_string[0:5])
print(hello_string[0:6])

# Basic slicing examples
print("Characters from index 0 to 5:", sample_str[0:5])  # Output: 'abcde'
print("Characters from index 0 to 5:", sample_str[25])  # Output: 'abcde'
print("Characters from index 0 to 25:", sample_str[0:25])  # Output: 'abcde'
# print("Characters from index 0 to 5:", sample_str[26])  # Output: 'abcde'

print("First 10 characters:", sample_str[:10])  # Output: 'abcdefghij'
print("Characters from index 10 to end:", sample_str[10:])  # Output: 'klmnopqrstuvwxyz'
print("Last 5 characters:", sample_str[-5:])  # Output: 'vwxyz'
print("All except last 3 characters:", sample_str[:-3])  # Output: 'abcdefghijklmnopqrstuvw'
print("All except first 3 characters:", sample_str[3:])  # Output: 'defghijklmnopqrstuvwxyz'

# Slicing with steps
print("Every second character:", sample_str[::2])  # Output: 'acegikmoqsuwy'
print("Every third character:", sample_str[::3])  # Output: 'adgjmpsvy'
print("Characters from index 5 to 15, every second:", sample_str[5:16:2])  # Output: 'fhjlnp'

# More easy examples of step operator (step in slicing)
print("Every fourth character:", sample_str[::4])  # Output: 'aeimquy'
print("Every fifth character:", sample_str[::5])  # Output: 'afkpuvz'
print("Every second character from index 1:", sample_str[1::2])  # Output: 'bdfhjlnprtvxz'
print("Every third character from index 2:", sample_str[2::3])  # Output: 'cfilorux'
print("Every second character in last 10 letters:", sample_str[-10::2])  # Output: 'qswuy'
print("Every third character in first 9 letters:", sample_str[:9:3])  # Output: 'adg'

# Negative slicing examples
print("Last 10 characters:", sample_str[-10:])  # Output: 'qrstuvwxyz'
print("Characters from -15 to -5:", sample_str[-15:-5])  # Output: 'lmnopqrstuv'
print("Every second character from -20 to -10:", sample_str[-20:-10:2])  # Output: 'klmoq'

# Reversing the string
print("Reverse the string:", sample_str[::-1])  # Output: 'zyxwvutsrqponmlkjihgfedcba'
print("Reverse first 5 characters:", sample_str[4::-1])  # Output: 'edcba'
print("Reverse last 5 characters:", sample_str[-1:-6:-1])  # Output: 'zyxwv'

# Slicing with omitted indices
print("Full string:", sample_str[:])  # Output: 'abcdefghijklmnopqrstuvwxyz'

# Edge cases
print("Empty slice (start > end):", sample_str[10:5])  # Output: ''
print("Slice with step -2 (reverse every second):", sample_str[::-2])  # Output: 'zxvtrpnljhfdb'
