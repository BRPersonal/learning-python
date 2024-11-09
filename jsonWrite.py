import json
from datetime import datetime

# Get the current timestamp
current_timestamp = datetime.now().strftime("%d-%b-%Y %H:%M:%S")

emp = {
        "name": "Balaji",
        "age": 50,
        "job": "Ok",
        "address": 
        {
            "doorNo" : "169/2",
            "street" : "East Uthra street",
            "city": "srirangam, Trichy",
            "state": "TamilNadu",
            "country": "India",
            "zip": "620 006"
        },
        "timeStamp" : current_timestamp
     }

with open("emp.json","w",encoding="utf-8") as f:
    json.dump(emp,f,indent=4)
print("Json written to file")
