#Day 11: Price Scraping and Cleaning

import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    with open("books_prices.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])

        for book in books:
            title = book.h3.a["title"]

            price_text = book.find("p", class_="price_color").text
            price_clean = price_text.replace("£", "").replace("Â","").strip()
            print(price_clean)
            writer.writerow([title, price_clean])

    print("Books prices saved successfully")

else:
    print("Failed to fetch page")

