"""
filter question

Use the filter function to extract cities with a population greater than 2 million.
"""


cities = [
    ("New York", 8500000),
    ("Los Angeles", 4000000),
    ("Chicago", 2700000),
    ("Houston", 2300000),
    ("choenix", 1600000),
    ("Philadelphia", 1500000),
    ("San Antonio", 1500000),
]



cities_gret_million = list(filter(lambda city : city[1]>2000000,cities))
cities_sartingwith_c = list(filter(lambda city : city[0][0].upper== 'C',cities))
print(cities_sartingwith_c)
print(cities_gret_million)

