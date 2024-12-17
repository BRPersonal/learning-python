import json

# Original JSON response
response_json = {
    "response": {
        "data": {
            "total_users": 9,
            "users": [
                {
                    "group": "Developer",
                    "user_id": 10,
                    "first_name": "Sai",
                    "last_name": "Ram",
                    "email": "smuralikrishnan@fleetstudio.com",
                    "usage": 18
                },
                {
                    "group": "adobe-express",
                    "user_id": 20,
                    "first_name": "Thangaraj",
                    "last_name": "news",
                    "email": "tmanthiriyappan+401@fleetstudio.com",
                    "usage": 7
                },
                {
                    "group": "Developer",
                    "user_id": 22,
                    "first_name": "Thangaraj",
                    "last_name": "news",
                    "email": "tmanthiriyappan+220@fleetstudio.com",
                    "usage": 5
                },
                {
                    "group": "adobe-express",
                    "user_id": 23,
                    "first_name": "Sai",
                    "last_name": "TestAdobe",
                    "email": "adbexp01@kimgmail.com",
                    "usage": 5
                },
                {
                    "group": "adobe-express",
                    "user_id": 25,
                    "first_name": "thangaraj",
                    "last_name": "test",
                    "email": "tmanthiriyappan+203@fleetstudio.com",
                    "usage": 5
                },
                {
                    "group": "wax-audit-chrome-extension",
                    "user_id": 27,
                    "first_name": "SaiChrome",
                    "last_name": "Testing",
                    "email": "3coeajfyvm@netveplay.com",
                    "usage": 5
                },
                {
                    "group": "adobe-express",
                    "user_id": 26,
                    "first_name": "thangaraj",
                    "last_name": "qwerty",
                    "email": "tmanthiriyappan+402@fleetstudio.com",
                    "usage": 3
                },
                {
                    "group": "wax-audit-chrome-extension",
                    "user_id": 24,
                    "first_name": "Thangaraj",
                    "last_name": "Fleetstudio",
                    "email": "tmanthiriyappan+650@fleetstudio.com",
                    "usage": 2
                },
                {
                    "group": "wax-audit-chrome-extension",
                    "user_id": 23,
                    "first_name": "Sai",
                    "last_name": "TestAdobe",
                    "email": "adbexp01@kimgmail.com",
                    "usage": 1
                }
            ]
        }
    },
    'status_code': '200',
    'message': 'Success'
}

# Transforming the response
transformed_response = {
    'response': {
        'data': {
            'total_users': response_json['response']['data']['total_users']
        }
    }
}

# Grouping users by their group
for user in response_json['response']['data']['users']:
    group = user['group']
    if group not in transformed_response['response']['data']:
        transformed_response['response']['data'][group] = []
    transformed_response['response']['data'][group].append({
        'user_id': user['user_id'],
        'first_name': user['first_name'],
        'last_name': user['last_name'],
        'email': user['email'],
        'usage': user['usage']
    })

# Print the transformed JSON
print(json.dumps(transformed_response, indent=4))
