import requests
from bs4 import BeautifulSoup
url = "https://otziv-otziv.ru/katalog/headphones/sennheiser-naushniki/sennheiser-cx-300-ii-otzyvy.html?page=73"
request = requests.get(url)
bs = BeautifulSoup(request.text, 'lxml')

reviews = bs.find_all('div', 'container-reviews collapsible collapsed')

numberOfReviews = 0
for review in reviews:
    numberOfReviews += 1

averageRating = bs.find('div', 'stars-container').get('title')[-1]

print(f"Количество отзывов на 73-ей странице = {numberOfReviews} штук")
print(f'Средняя оценка этого продукта = {averageRating}')