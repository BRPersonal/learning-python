#demo of python's powerful feature match-case
from typing import Optional,List,Any
import json


def parse_response(json_response:str) -> Optional[List[Any]]:
    response_data = json.loads(json_response)
    print(f"response type={type(response_data).__name__}")

    match response_data:
        # Case 1: Success (Matches specific keys AND values)
        case {"status": 200, "data": {"result": results}}:
            print(f"Success! Processed {len(results)} files.")
            return results

        # Case 2: Error (Captures the error message and retry time)
        case {"status": 500, "error": msg, "retry_after": time}:
            print(f"Failed: {msg}. Retrying in {time}s...")
            return None

        # Case 3: Legacy List (Matches any list of integers, if < 10)
        case [first, *rest] if len(rest) < 9:
            print(f"Processing small batch starting with {first}")
            return json_response

        #Case 4: catch all
        case _:
            print("Invalid response format.")
            return None


response_1 = """
{
    "status": 200,
    "data": {
        "job_id": 101,
        "result": ["file_a.csv", "file_b.csv"]
    }
}
"""

#Note U could also use 3 consecutive single quote to mark a docstring
response_2 = '''
{
    "status": 500,
    "error": "Timeout",
    "retry_after": 30
}
'''

response_3 = "[101, 102, 103]"
response_4 = "[101, 102, 103,101, 102, 103,101, 102, 103,101, 102, 103]"


if __name__ == "__main__":
    result = parse_response(response_1)
    print(result,"\n","-" * 30)

    result = parse_response(response_2)
    print(result,"\n","-" * 30)

    result = parse_response(response_3)
    print(result,"\n","-" * 30)

    result = parse_response(response_4)
    print(result,"\n","-" * 30)
