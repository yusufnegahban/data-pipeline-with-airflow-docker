# Fetches book data from Google Books API. 📚🚀
import time
import requests
from requests.exceptions import RequestException
from .models import Book
from app import db
from . import create_app

def scrape_books_from_google_api(query="python programming", max_pages=1):
    print("📚 Scraping started...")
    base_url = "https://www.googleapis.com/books/v1/volumes"
    books_added = 0

    def get_isbn(volume_info):
        for identifier in volume_info.get('industryIdentifiers', []):
            if identifier.get('type') == 'ISBN_13':
                return identifier.get('identifier')
        return 'Unknown ISBN'

    for page in range(max_pages):  # 
        params = {
            'q': query,
            'startIndex': page * 10,
            'maxResults': 10,
            'key': 'AIzaSyDEDtwCd-qLtx-3RiKaVIc4o4sK1ChZfmU'  # API Key
        }

        try:
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            print("API response:", data)
        except RequestException as e:
            print(f"❌ Error fetching page {page + 1}: {e}")
            continue

        for item in data.get('items', []):
            print("Processing item:", item)
            volume_info = item.get('volumeInfo', {})
            sale_info = item.get('saleInfo', {})

            title = volume_info.get('title', 'Unknown Title')
            authors = volume_info.get('authors', ['Unknown Author'])
            published_date = volume_info.get('publishedDate', '')
            isbn = get_isbn(volume_info)
            price = 0.0

            if sale_info.get('saleability') == 'FOR_SALE':
                price = sale_info.get('listPrice', {}).get('amount', 0.0)

            if Book.query.filter_by(title=title, author=authors[0]).first():
                continue

            new_book = Book(
                title=title,
                author=authors[0],
                published_date=published_date,
                isbn=isbn,
                price=price
            )
            db.session.add(new_book)
            books_added += 1

        time.sleep(2)

    db.session.commit()
    print(f"✅ {books_added} new books scraped and stored.")

    if books_added == 0:
        print("⚠️ No new books were added.")

# ✅ Test 
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        scrape_books_from_google_api(query="python programming", max_pages=1)
