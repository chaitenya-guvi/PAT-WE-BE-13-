"""

| Exception               | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `TypeError`             | Raised when an operation uses incompatible data types        |
| `ValueError`            | Raised when a function receives a valid type but wrong value |
| `UnicodeError`          | Error related to Unicode operations                          |
| `UnicodeEncodeError`    | Unicode encoding failure                                     |
| `UnicodeDecodeError`    | Unicode decoding failure                                     |
| `UnicodeTranslateError` | Unicode translation failure                                  |



"""
#example of TypeError

try:
    result = '2' + 2  # This will raise a TypeError
except TypeError:
    print("Error: unsupported operand type(s) for +: 'str' and 'int'.")
else:
    print("Result:", result)

# example of ValueError
try:
    number = int("abc")  # This will raise a ValueError
except ValueError:
    print("Error: invalid literal for int() with base 10: 'abc'.")
else:
    print("Number:", number)
