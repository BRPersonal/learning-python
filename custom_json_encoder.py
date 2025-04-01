import json
from datetime import date,datetime
from decimal import Decimal


class CustomJSONEncoder(json.JSONEncoder):
    """Custom serializer to handle non-serializable types."""


    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()  # Convert datetime to ISO 8601 string
        elif isinstance(obj, Decimal):
            return float(obj)  # Convert Decimal to float
        else:
            return super().default(obj)



