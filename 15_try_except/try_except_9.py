"""
try: Code that might cause an error

except: Runs only if an error occurs

else: Runs only if no error occurs in the try

finally: Always runs, whether there is an error or not

"""

numbers = [10, 20, 30]

try:
    value = numbers[5]        # Trying to access index 1
except IndexError:
    print("Index does not exist in the list.")
else:
    print("Value found:", value)
finally:
    print("List access attempt complete.")
