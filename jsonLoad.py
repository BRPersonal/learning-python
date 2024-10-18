#This assumes emp.json exists in this directory
#To create emp.json run jsonwrite.py

import json

with open("emp.json","r",encoding="utf-8") as f:
    emp = json.load(f)
    print("Json loaded from file")
    print(f"type of object loaded={type(emp)}")
    name = emp["name"]
    pincode = emp["address"]["zip"]
    print(f"name={name}, zip={pincode}")
