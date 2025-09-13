#explicit type conversion

# Float to int

float_numer = 5.99999
type_casted_variable = int(float_numer)  # Result: 5 (decimal part is truncated, not rounded)
print(type_casted_variable)

print('@'*20)

# String to int
string1 = "123"
print(string1)
print(type(string1))

print('@'*20)
#explicitalyy converting string
type_casted_string1 = int(string1)  # Result: 123
print(type_casted_string1)
print(type(type_casted_string1))

print('@'*20)
# Boolean to int
print(int(True))   # Output: 1
print(int(False))  # Output: 0

# Additional examples: String to int conversion
print('@'*20)
# String with leading/trailing spaces
string2 = "   456  "
type_casted_string2 = int(string2.strip())  # strip() removes spaces
print(f"Original: '{string2}' | Converted: {type_casted_string2} | Type: {type(type_casted_string2)}")

# Negative number string
string3 = "-789"
type_casted_string3 = int(string3)
print(f"Original: '{string3}' | Converted: {type_casted_string3} | Type: {type(type_casted_string3)}")

# String with leading zeros
string4 = "007"
type_casted_string4 = int(string4)
print(f"Original: '{string4}' | Converted: {type_casted_string4} | Type: {type(type_casted_string4)}")
