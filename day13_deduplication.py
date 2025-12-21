#Day 13: Deduplication and Robust Scraping

import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        return[]
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    data = []
    for book in books:
        title = book.h3.a["title"]

        price_tag = book.find("p", class_="price_color")
        if not price_tag:
            continue

        price_text = price_tag.text
        price = float(price_text.replace("£", "").replace("Â", "").strip())

        data.append((title, price))

    return data

all_books = set()
total_scraped = 0

#Page 1
print("---- PAGE 1 ----")
for item in scrape_page("https://books.toscrape.com/"):
    total_scraped += 1
    all_books.add(item)

#Page 2-5
for page in range(2, 6):
    print("---- PAGE", page, "----")
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    for item in scrape_page(url):
        total_scraped += 1
        all_books.add(item)

with open("books_prices_unique.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])

    for title, price in all_books:
        writer.writerow([title, price])

print("Total scraped (with duplicates):", total_scraped)
print("Total unique books:", len(all_books))
print("Duplicates removed:", total_scraped - len(all_books))


