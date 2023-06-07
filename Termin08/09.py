"""
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
"""
import json

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ("running", "sky diving", "singing"),
    "age": 35,
    "children": [{"firstName": "Alice", "age": 6}, {"firstName": "Bob", "age": 8}],
}

# json_data = json.dumps(data)
# print(json_data)
# '{"firstName": "Jane", "lastName": "Doe", "hobbies": ["running", "sky diving", "singing"], "age": 35, "children": [{"firstName": "Alice", "age": 6}'

# py_data = json.loads(json_data)
# print(py_data)

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)

with open("data_file.json", "r") as read_file:
    data2 = json.load(read_file)
    print(data2)
