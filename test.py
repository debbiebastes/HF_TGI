import requests

headers = {
    "Content-Type": "application/json",
}

data = {
    'inputs': 'Who were the first five presidents of the USA, chronologically?',
    'parameters': {
        'max_new_tokens': 400,
    },
}

response = requests.post('http://127.0.0.1:8080/generate', headers=headers, json=data)
print(response.json())