import requests
from bs4 import BeautifulSoup
import json

# URL сайту для скрапінгу
url = "http://quotes.toscrape.com"

# Отримати вміст сторінки
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Ініціалізувати пусті списки для цитат та авторів
quotes_data = []
authors_data = []

# Цикл для обробки кожної сторінки
while True:
    # Отримати інформацію про цитати та авторів на поточній сторінці
    for quote_box in soup.find_all('div', class_='quote'):
        quote_text = quote_box.find('span', class_='text').text
        author_name = quote_box.find('small', class_='author').text
        author_url = 'http://quotes.toscrape.com' + quote_box.find('a').get('href')
        
        quotes_data.append({
            'text': quote_text,
            'author': author_name
        })

        # Додати інформацію про автора до списку авторів, якщо її ще немає
        if not any(author['name'] == author_name for author in authors_data):
            authors_data.append({
                'name': author_name,
                'profile_url': author_url
            })

    # Перейти на наступну сторінку (якщо вона є)
    next_page = soup.find('li', class_='next')
    if next_page:
        next_page_url = url + next_page.find('a')['href']
        response = requests.get(next_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        break

# Зберегти отримані дані у JSON файли
with open('quotes.json', 'w', encoding='utf-8') as quotes_file:
    json.dump(quotes_data, quotes_file, ensure_ascii=False, indent=4)

with open('authors.json', 'w', encoding='utf-8') as authors_file:
    json.dump(authors_data, authors_file, ensure_ascii=False, indent=4)
