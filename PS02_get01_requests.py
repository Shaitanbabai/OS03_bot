import requests

params = {
    'q': 'html'
}

response = requests.get('https://api.github.com/search/repositories', params=params)

response_json = response.json()
print(f"number of repositories using html: {response_json['total_count']}")

print(response.status_code)
