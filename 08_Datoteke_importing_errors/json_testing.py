import json

data = {
    "company":{
        "employees": [
            {"name":"emma",
            "payble":{
                "salary":7000,
                "bonus":800
            }},
            {"name":"derek",
                "payble":{
                    "salary":4000,
                    "bonus":1000
            }},
            {"name":"alex",
                "payble":{
                    "salary":7500,
                    "bonus":500
            }},
            {"name":"susan",
                "payble":{
                    "salary":6300,
                    "bonus":350
            }},
            {"name":"martha",
                "payble":{
                    "salary":9100,
                    "bonus":1200
            }},
            {"name":"clark",
                "payble":{
                    "salary":7700,
                    "bonus":270
            }},
            {"name":"luise",
                "payble":{
                    "salary":8200,
                    "bonus":900
            }}
        ]
    }
}

json_data = json.dumps(data)
# print(type(json_data))
# print(json_data)

py_data = json.loads(json_data)
print(type(py_data))
print(py_data)