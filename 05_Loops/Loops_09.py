# More examples of while loop in Python with meaningful variable names

# Example 1: Countdown from 5 to 1
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off!")

# Example 2: Sum numbers until total reaches or exceeds 20
current_number = 1
total_sum = 0
while total_sum < 20:
    print(f"Adding {current_number} to total {total_sum}")
    total_sum += current_number #adding current number to total sum
    current_number += 1 #incrementing the current number
print(f"Final total: {total_sum}")

# Example 3: Print all even numbers less than 10
number = 2
while number < 10:
    print(f"Even number: {number}")
    number += 2 #incrementing by 2 to get the next even number

# Example 4: Loop until a condition is met (simulate user input)
# Uncomment below to test interactively
password = ""
while password != "python123":
    password = input("Enter the password: ")
print("Access granted!")

# Example 5: Loop through a list using while
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print(f"Fruit: {fruits[index]}")
    index += 1

