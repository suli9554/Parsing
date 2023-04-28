import requests
from bs4 import BeautifulSoup

url = "https://otziv-otziv.ru/katalog/headphones/sennheiser-naushniki/sennheiser-cx-300-ii-otzyvy.html?page=73"
request = requests.get(url)
bs = BeautifulSoup(request.text, 'lxml')
productName = bs.find('h1')
print(productName.text)
print(productName.get_text())

reviews = bs.find_all('div', 'container-reviews collapsible collapsed')

numberOfReviews = 0
for review in reviews:
    numberOfReviews += 1

for review in reviews:
    reviewAuthor = review.find('span', 'user').get_text()
    reviewDate = review.find('span', 'date').get_text()
    reviewStars = review.find('div', 'stars-container').get('title')[-1]
    reviewText = review.find_all('p')
    print("Author: ", reviewAuthor)
    print("Date: ", reviewDate)
    print("Stars: ", reviewStars)
    print("Comment: ")
    for elem in reviewText:
        print(elem.get_text())


averageRating = bs.find('div', 'stars-container').get('title')[-1]

print(f"Количество отзывов на 73-ей странице = {numberOfReviews} штук")
print(f'Средняя оценка этого продукта = {averageRating}')
#Не смог коменты вывести

