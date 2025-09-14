string1 = "Python"

print(string1)
print(f"string at index 0 , counting 1  is :  {string1[0]}") # Output: 'P'
print(f"string at index 1 , counting 2  is :  {string1[1]}") # Output: 'y'
print(f"string at index 2 , counting 3  is :  {string1[2]}") # Output: 't'
print(f"string at index 3 , counting 4  is :  {string1[3]}") # Output: 'h'
print(f"string at index 4 , counting 5  is :  {string1[4]}") # Output: 'o'
print(f"string at index 5 , counting 6  is :  {string1[5]}") # Output: 'n'
print("--------------------------------------------------")
#slicing with step
print(f"Every second character: {string1[::2]}")  # Output: 'Pto'
print(f"Every third character: {string1[::3]}")  # Output: 'Ph'
print(f"Characters from index 1 to 5, every second: {string1[1:6:2]}")  # Output: 'yhn'
print(f"Characters from index 0 to 5, every second: {string1[0:6:2]}")  # Output: 'Pto'
print(f"Characters from index 0 to 4, every second: {string1[0:6:2]}")  # Output: 'Pto'

print("--------------------------------------------------")

print(f"string at index -1 , counting 1 from last  is :  {string1[-1]}") # Output: 'n'
print(f"string at index -2 , counting 2 from last  is :  {string1[-2]}") # Output: 'o'
print(f"string at index -3 , counting 3 from last  is :  {string1[-3]}") # Output: 'h'
print(f"string at index -4 , counting 4 from last  is :  {string1[-4]}") # Output: 't'
print(f"string at index -5 , counting 5 from last  is :  {string1[-5]}") # Output: 'y'
print(f"string at index -6 , counting 6 from last  is :  {string1[-6]}") # Output: 'P'
print("--------------------------------------------------")


#step with negative value
print(f"normal string : {string1[::]}")
print(f"normal string : {string1[::1]}")
print(f"Reverse the string: {string1[::-1]}")  # Output: 'nohtyP'
print(f"Reverse first 3 characters: {string1[2::-1]}")  # Output: 'tP'
print(f"Reverse last 3 characters: {string1[-1:-4:-1]}")  # Output: 'noh'
print(f"Every second character in reverse: {string1[::-2]}")  # Output: 'nt
