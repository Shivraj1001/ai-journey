import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_= "quote")

    file = open("quotes.txt", "w", encoding="utf-8")

    for index, quote in enumerate(quotes, start=1):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        
        file.write(str(index)+". " + text + " - " + author.upper() + "\n\n")

    file.close()
    print("Quotes saved successfully")

else:
    print("Failed to fetch page")