import json

with open('./files/json_example.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    print(type(data))  # <class 'dict'>

print(data['skills'])