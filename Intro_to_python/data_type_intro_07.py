#explicit type conversion

# Float to int

a = 5.99999
b = int(a)  # Result: 5 (decimal part is truncated, not rounded)
print(b)

# String to int
s = "123"
print(s)
print(type(s))

n = int(s)  # Result: 123
print(n)
print(type(n))

# Boolean to int
print(int(True))   # Output: 1
print(int(False))  # Output: 0
