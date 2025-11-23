"""
| Exception          | Description            |
| ------------------ | ---------------------- |
| `SyntaxError`      | Invalid Python syntax  |
| `IndentationError` | Incorrect indentation  |
| `TabError`         | Mixing spaces and tabs |


"""
#example of SyntaxError
try:
    eval('x === x')  # This will raise a SyntaxError
except SyntaxError:
    print("Error: invalid syntax.")
else:
    print("Code executed successfully.")

# example of IndentationError
try:
    exec('def func():\nprint("Hello")')  # This will raise an IndentationError
except IndentationError:
    print("Error: unexpected indent.")
else:
    print("Function defined successfully.")
