import json
from datetime import date,datetime
from decimal import Decimal

from custom_json_encoder import CustomJSONEncoder

input_data = [
    {
        "id": 1,
        "name": "Alice",
        "birth_date": date(1995,8,25),                 #"1995-08-25",
        "timestamp":  datetime(2024,3,12,15,30,25),    #"2024-03-12T15:30:25",
        "salary": Decimal(75000.5),
        "binary_data": "hello world",
        "nested_list": [1, 2, Decimal(3.14), datetime(2024,3,12,15,0,0)],      #"2024-03-12T15:00:00"
        "nested_dict": {
            "key1": "value1",
            "key2": Decimal(99.99),
            "sub_dict": {"sub_key": "2023-05-17"}
        }
    },
    {
        "id": 2,
        "name": "Bob",
        "birth_date": "1990-01-10",
        "timestamp": "2024-03-12T16:30:00",
        "salary": 62000.75,
        "nested_list": [
            {"value": 45.67},
            {"timestamp": "2024-03-12T17:00:00"}
        ]
    }
]



# Serialize using the custom encoder
json_data = json.dumps(input_data, cls=CustomJSONEncoder,indent=4)
print(json_data)

#Deserialize from string
result = json.loads(json_data)
print(result)


