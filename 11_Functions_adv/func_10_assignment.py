"""
map question

Write a Python program to convert all the characters into uppercase
and eliminate duplicate letters from a given sequence. Use the map() function.
"""

def change_cases(s):
  return str(s).upper()



chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n",chars)

result = map(change_cases, chars)
result_no_duplicate = set(result)

print(f"\nAfter converting above characters in upper \nand eliminating duplicate letters: {result_no_duplicate}")
