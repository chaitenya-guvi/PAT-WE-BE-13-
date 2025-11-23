"""
| Exception           | Description                                    |
| ------------------- | ---------------------------------------------- |
| `IndexError`        | Index out of range in a sequence (list, tuple) |
| `KeyError`          | Key not found in a dictionary                  |
| `AttributeError`    | Attribute or method not found for an object    |
| `NameError`         | Variable name not found                        |
| `UnboundLocalError` | Local variable referenced before assignment    |
| `LookupError`       | Base class for IndexError and KeyError         |

"""

# example of IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise an IndexError
except IndexError:
    print("Error: list index out of range.")
else:
    print("List item:", my_list[5])

# example of KeyError
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])  # This will raise a KeyError
except KeyError:
    print("Error: 'c' key not found in dictionary.")
else:
    print("Dictionary value:", my_dict['c'])
