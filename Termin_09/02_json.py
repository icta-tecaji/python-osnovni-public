'''
{"firstName": "Jane","lastName": "Doe","hobbies": ["running", "sky diving", "singing"],"age": 35,"children": [{"firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
'''
import json
data = {
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

with open("data_file.json", "w") as f:
    json.dump(data, f)


with open("data_file.json", "r") as f:
    data2 = json.load(f)
    print(data)
    print(type(data))
    print(data["firstName"])