import requests
import pprint

# params = {
#     'q': 'python'
# }
#
# response = requests.get('https://api.github.com/search/repositories', params=params)
#
# # print(response.status_code)
# # print(response.ok)
# # if response.ok:
# #     print('запрос успешно выполнен')
# # else:
# #     print('произошла ошибка')
#
# response_json = response.json()
# print(f"number of repositories using js: {response_json['total_count']}")
img = "https://cdn.fishki.net/upload/post/2019/11/16/3142084/tn/36a850408d17dcc695fecb0c9111b733.jpg"

response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)
