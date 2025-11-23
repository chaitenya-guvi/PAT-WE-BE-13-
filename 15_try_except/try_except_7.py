"""
| Exception             | Description                                         |
| --------------------- | --------------------------------------------------- |
| `ImportError`         | Raised when a module cannot be imported             |
| `ModuleNotFoundError` | Specific type of ImportError when module is missing |

"""

# example of ImportError
try:
    import non_existent_module  # This will raise an ImportError
except ImportError:
    print("Error: module could not be imported.")
else:
    print("Module imported successfully.")

# example of ModuleNotFoundError
try:
    import another_missing_module  # This will raise a ModuleNotFoundError
except ModuleNotFoundError:
    print("Error: module not found.")
else:
    print("Module found and imported successfully.")

