import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL inside Docker
engine = create_engine("postgresql+psycopg2://airflow:securepass123@postgres:5432/airflow")

query = """
SELECT * FROM books
WHERE run_date >= CURRENT_DATE - INTERVAL '7 days';
"""

df = pd.read_sql(query, con=engine)
df.to_csv("/opt/airflow/books_last_week.csv", index=False)

print("✅ Exported books to /opt/airflow/books_last_week.csv")
