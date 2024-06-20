from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)
html = response.text  # объект для передачи кода html

soup = BeautifulSoup(html, "html.parser")  # объект для работы с библиотекой и html-парсеом

# links = soup.find_all("a")
#
# for link in links:
#     print(link.get('href'))  # получение содержимого из атрибута href
text = soup.find_all("span", class_="text")  # find находит первый попавшийся фрагемент n\
# на сайте, имеющий в коде тэг span и класс text, а find_all ищет всё
# print(text)
author = soup.find_all("small", class_="author")
# print(author)

for i in range(len(text)):  # перебираем по всей длине текст
    print(f"Цитата номер {i+1}")  # присвоив порядковый номер
    print(text[i].text)  # выводим текст
    print(f"Автор цитаты - {author[i].text}\n")  # и имя автора, а n\ дает отступ между цитатами
