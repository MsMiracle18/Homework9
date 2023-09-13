import pymongo
import json

# Підключення до MongoDB
client = pymongo.MongoClient("host='mongodb+srv://ms_miracle18:ryPanrIWBPIoqX0T@cluster0.d6hdlvu.mongodb.net/")
db = client["mydatabase"]

# Завантаження даних з quotes.json
with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
    quotes_data = json.load(quotes_file)

# Завантаження даних з authors.json
with open('authors.json', 'r', encoding='utf-8') as authors_file:
    authors_data = json.load(authors_file)

# Додавання цитат до колекції цитат
quotes_collection = db["quotes"]
quotes_collection.insert_many(quotes_data)

# Додавання авторів до колекції авторів
authors_collection = db["authors"]
authors_collection.insert_many(authors_data)
