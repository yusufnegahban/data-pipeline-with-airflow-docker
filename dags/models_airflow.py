# /opt/airflow/dags/models_airflow.py
from sqlalchemy import Column, Integer, String, Date , Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# Match the PostgresHook connection
DATABASE_URL = "postgresql://airflow:securepass123@postgres:5432/airflow"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Book(Base):
    __tablename__ = 'books'

    run_date = Column(Date, default=date.today)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300))
    price = Column(Float)
    availability = Column(String(50))  # added for example
    published_date = Column(Date)
    isbn = Column(String(100))

# Create table automatically
Base.metadata.create_all(bind=engine)
