import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(url, writer):
    response = requests.get(url)

    if response.status_code != 200:
        return False
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price_tag = book.find("p", class_="price_color")
        if price_tag is None:
            continue

        price_text = price_tag.text
        price = float(price_text.replace("£", "").replace("Â", "").strip())
        writer.writerow([title, price])
    return True

with open("books_prices_pages.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])

    #Page 1 (special case)
    scrape_page("https://books.toscrape.com/", writer)

    #Page 2 to 5
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"

    for page in range(2,6):
        url = base_url.format(page)
        success = scrape_page(url, writer)

        if not success:
            break

print("Multiple pages scraped successfully")