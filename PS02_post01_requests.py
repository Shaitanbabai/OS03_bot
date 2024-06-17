import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Заголовок записи",
    "body": "Текст записи",
    "userId": 1
}

response = requests.post(url, json=data)

print(f"Статус код: {response.status_code}")

print("Ответ:")

print(response.json())
