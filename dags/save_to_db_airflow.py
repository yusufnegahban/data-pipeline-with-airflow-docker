from models_airflow import Book
from datetime import date  # Added for run_date
from datetime import datetime


def run_saver(books, hook=None):
    if hook:
        conn = hook.get_conn()
        cursor = conn.cursor()
    else:
        session = SessionLocal()

    added = 0
    try:
        for b in books:
            # Safe defaults for missing fields
            title = b.get("title", "Unknown")
            author = b.get("author", "Unknown")
            published_date = b.get("published_date", None)
            isbn = b.get("isbn", "N/A")
            price = b.get("price", "0.00")
        
            run_date = datetime.now().date()  
            # More precise
  # Track the DAG execution date

            if hook:
                    cursor.execute(
                       """
                       INSERT INTO books (title, author, published_date, run_date, isbn, price, download_time)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                       """,
                     (title, author, published_date, run_date, isbn, price, datetime.now().time())
                     )
            else:
                exists = session.query(Book).filter_by(title=title, author=author).first()
                if exists:
                    continue
                new_book = Book(
                    title=title,
                    author=author,
                    published_date=published_date,
                    isbn=isbn,
                    price=price,
                    run_date=run_date
                )
                session.add(new_book)
            added += 1

        if hook:
            conn.commit()
            cursor.close()
            conn.close()
        else:
            session.commit()

        print(f"✅ {added} books saved to database.")
    except Exception as e:
        if hook:
            conn.rollback()
        else:
            session.rollback()
        print(f"❌ Error saving books: {e}")
    finally:
        if not hook:
            session.close()
