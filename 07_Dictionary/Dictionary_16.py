"""

dictionary method
setdefaults
"""

# dictionary method
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
# setdefaults
my_dict.setdefault("name", "Jane")
my_dict.setdefault("country", "USA")
print(my_dict)
# set default method is used to set a default value for a key in a dictionary.
# If the key already exists, it does nothing. If the key does not exist, it adds the key with the specified default value.
