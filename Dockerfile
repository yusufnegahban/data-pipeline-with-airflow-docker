# airflow/Dockerfile

# Use official Airflow image
FROM apache/airflow:2.9.1

# Set working directory
WORKDIR /opt/airflow

# Copy DAGs into Airflow container
COPY dags /opt/airflow/dags

# Copy entire app folder (شامل scraper.py و سایر فایل‌ها)
COPY ../app /opt/airflow/app

# Install Python dependencies used in scraper.py
RUN pip install --no-cache-dir requests flask sqlalchemy

# Set PYTHONPATH to include /opt/airflow/app so scraper.py و مدل‌ها پیدا بشن
ENV PYTHONPATH="/opt/airflow/app:${PYTHONPATH}"





# airflow/Dockerfile

# Use official Airflow image
#FROM apache/airflow:2.9.1

# Set working directory
#WORKDIR /opt/airflow

# Copy DAGs into Airflow container
#COPY dags /opt/airflow/dags

# Copy scraper.py from app folder into DAGs folder
#COPY ../app/scraper.py /opt/airflow/dags/
