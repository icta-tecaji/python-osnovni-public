import json

data={"first name":"Jane",
      "last name":"Doe",
      "hobbies":["running","sky diving","singing"],
      "age":35}


json_data=json.dumps(data)
print(json_data)
print(type(json_data))

py_data=json.loads(json_data)
print(py_data)
print(type(py_data))