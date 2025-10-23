# test_saver.py
from airflow.providers.postgres.hooks.postgres import PostgresHook

# Dummy books
books = [
    {"title": "Test Book", "price": 19.99, "availability": "In stock"}
]

# Connect using your Airflow connection
hook = PostgresHook(postgres_conn_id="postgres_default")
conn = hook.get_conn()
cursor = conn.cursor()

for book in books:
    cursor.execute(
        "INSERT INTO books (title, price, availability) VALUES (%s, %s, %s)",
        (book["title"], book["price"], book["availability"])
    )

conn.commit()
cursor.close()
conn.close()
print("✅ Test book saved via PostgresHook")
