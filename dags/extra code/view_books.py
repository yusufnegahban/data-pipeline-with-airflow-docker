import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL inside Docker
engine = create_engine("postgresql+psycopg2://airflow:securepass123@postgres:5432/airflow")

# Query all books
query = "SELECT * FROM books ORDER BY run_date DESC;"

# Load into DataFrame
df = pd.read_sql(query, con=engine)

# Print nicely
print(df.to_markdown(tablefmt="grid"))
