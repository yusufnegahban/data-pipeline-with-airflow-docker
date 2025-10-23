import time
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import hashlib

def scrape_books_from_toscrape(max_pages=1):
    print("📚 Scraping started...")
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    books = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        for attempt in range(3):
            try:
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                break  # success
            except RequestException as e:
                print(f"⚠️ Attempt {attempt+1} failed on page {page}: {e}")
                time.sleep(2)
        else:
            print(f"❌ Skipping page {page} after 3 failed attempts")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("article.product_pod")

        for item in items:
            title = item.h3.a["title"]
            raw_price = item.select_one(".price_color").text
            clean_price = raw_price.encode('latin1').decode('utf-8').replace("£", "").strip()
            price = float(clean_price)
            availability = item.select_one(".availability").text.strip()
            published_date = "2025-01-01" 

            # default or dummy value
            isbn = hashlib.md5(title.encode()).hexdigest()[:10]

            books.append({
                "title": title,
                "price": price,
                "availability": availability,
                "published_date": published_date,
                "isbn": isbn
            })

        time.sleep(1)  # be polite

    print(f"✅ Scraped {len(books)} books")
    print(books)
    return books
