"""
Predefined exceptions -

| Exception            | Description                                      |
| -------------------- | ------------------------------------------------ |
| `ArithmeticError`    | Base class for math-related errors               |
| `ZeroDivisionError`  | Raised when dividing by zero                     |
| `OverflowError`      | Raised when a calculation exceeds numeric limits |
| `FloatingPointError` | Raised for floating-point operation failure      |

"""

# example of OverflowError
import math
try:
    result = math.exp(1000)  # This will likely cause an OverflowError
except OverflowError:
    print("Error: numerical result out of range.")
else:
    print("Result:", result)

