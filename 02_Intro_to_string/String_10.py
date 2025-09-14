string1 = "Python"
print(string1)
print(f"string at index 0 , counting 1  is :  {string1[0]}") # Output: 'P'
print(f"string at index 1 , counting 2  is :  {string1[1]}") # Output: 'y'
print(f"string at index 2 , counting 3  is :  {string1[2]}") # Output: 't'
print(f"string at index 3 , counting 4  is :  {string1[3]}") # Output: 'h'
print(f"string at index 4 , counting 5  is :  {string1[4]}") # Output: 'o'
print(f"string at index 5 , counting 6  is :  {string1[5]}") # Output: 'n'
print("--------------------------------------------------")
print(f"string at index -1 , counting 1 from last  is :  {string1[-1]}")
print(f"string at index -2 , counting 2 from last  is :  {string1[-2]}")
print(f"string at index -3 , counting 3 from last  is :  {string1[-3]}")
print(f"string at index -4 , counting 4 from last  is :  {string1[-4]}")
print(f"string at index -5 , counting 5 from last  is :  {string1[-5]}")
print(f"string at index -6 , counting 6 from last  is :  {string1[-6]}")
print("--------------------------------------------------")


# Slicing examples
# end index is excluded
print(f"Characters from index 0 to 3: {string1[0:4]}")  # Output: 'Pyth'


print(f"Characters from index 2 to end: {string1[2:]}")  # Output: 'thon'
