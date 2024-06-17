import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "test post-request",
    "body": "request body",
    "userID": 2
}

response = requests.post(url, data=data)

print(response.status_code)

print(f"ответ - {response.json()}")
