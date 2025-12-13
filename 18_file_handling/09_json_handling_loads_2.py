"""
Converting Json to Dictionary
"""

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

list_json = '''[
    {
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "skills": ["JavaScrip", "React", "Python"]
    },
    {
        "name": "David",
        "country": "UK",
        "city": "London",
        "skills": ["Java", "Spring", "Hibernate"]
    },
    {
        "name": "John",
        "country": "Sweden",
        "city": "Stockholm",
        "skills": ["C#", ".Net", "Azure"]
    }
]'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


# let's change JSON to list
people_lst = json.loads(list_json)
print(type(people_lst))
print(people_lst)
print(people_lst[0])