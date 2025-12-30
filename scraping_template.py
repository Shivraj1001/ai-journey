import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

# ================= CONFIG =================
BASE_URL = "https://quotes.toscrape.com/page/1/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 10
DELAY_SECONDS = 1
OUTPUT_FILE = "adv5-1.xlsx"
MAX_PAGES = None 


# ============== FETCH =====================
def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if response.status_code != 200:
            return None
        return response.text
    except requests.exceptions.RequestException:
        return None


# ============== PARSE =====================
def parse_items(html):
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    records = []
    for q in quotes:
        records.append({
            "quote": q.find("span", class_="text").get_text(strip=True)
                     if q.find("span", class_="text") else None,
            "author": q.find("small", class_="author").get_text(strip=True)
                      if q.find("small", class_="author") else None,
            "tags": ", ".join(tag.get_text(strip=True)
                              for tag in q.find_all("a", class_="tag"))
        })

    next_li = soup.find("li", class_="next")
    next_url = None
    if next_li:
        next_url = urljoin(BASE_URL, next_li.find("a")["href"])

    return records, next_url


# ============== CLEAN =====================
def clean_records(records):
    df = pd.DataFrame(records)
    return df


# ============== SAVE ======================
def save_excel(df):
    df.to_excel(OUTPUT_FILE, index=False)


# ============== MAIN ======================
def main():
    url = BASE_URL
    page = 1
    all_records = []

    while url:
        if MAX_PAGES and page > MAX_PAGES:
            break

        html = fetch_page(url)
        if not html:
            break

        records, next_url = parse_items(html)
        if not records:
            break

        all_records.extend(records)
        url = next_url

        page += 1
        time.sleep(DELAY_SECONDS)

    df = clean_records(all_records)
    save_excel(df)
    print("Scraping completed successfully")


if __name__ == "__main__":
    main()
