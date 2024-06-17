import requests

# URL API с параметром userId=1
url = "https://jsonplaceholder.typicode.com/posts?userId=1"

response = requests.get(url)

if response.status_code == 200:
    print("Запрос выполнен успешно!")
else:
    print(f"Ошибка запроса: {response.status_code}")
    