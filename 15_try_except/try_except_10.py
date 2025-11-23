"""
try: Code that might cause an error

except: Runs only if an error occurs

else: Runs only if no error occurs in the try

finally: Always runs, whether there is an error or not

"""

text = "Python"

try:
    number = int(text)        # Trying to convert a string to a number
except ValueError:
    print("Cannot convert text to a number.")
else:
    print("Conversion successful:", number)
finally:
    print("String conversion attempt finished.")
