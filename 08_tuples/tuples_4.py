# tuples_4.py

# Use tuples as keys in a dictionary
# Tuples are immutable, so they can be used as keys in dictionaries
location_data = {
    (40.7128, -74.0060): "New York",  # Coordinates as key
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago"
}

print("Location Data Dictionary:", location_data)
# Accessing values using tuple keys
ny_location = location_data[(40.7128, -74.0060)]
print("Location for (40.7128, -74.0060):", ny_location)

# Using tuples to group related data
person_info = {
    (1, "Alice"): {"age": 30, "city": "New York"},
    (2, "Bob"): {"age": 25, "city": "Los Angeles"},
    (3, "Charlie"): {"age": 35, "city": "Chicago"}
}

print("Person Info Dictionary:", person_info)

# create dictionary with single element tuple as key
single_element_tuple_dict = {
    (1,): "One",
    (2,): "Two",
    (3,): "Three"
}
print("Single Element Tuple Dictionary:", single_element_tuple_dict)

# access values from single element tuple dictionary
print("Value for key (1,):", single_element_tuple_dict[(1,)])
print("Value for key (2,):", single_element_tuple_dict[(2,)])

