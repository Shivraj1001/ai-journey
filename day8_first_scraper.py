import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")

    for index, quote in enumerate(quotes, start=1):
        print(index, quote.text)

else:
    print("Failed to fetch page")