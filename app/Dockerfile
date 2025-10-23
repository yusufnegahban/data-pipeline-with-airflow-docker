# Use Python 3.10 slim as the base image
FROM python:3.10-slim

# Set Docker working directory to /app
WORKDIR /app

# Copy requirements.txt from project root into /app
COPY requirements.txt /app/

# Install all dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy all application code (inside the app folder) into /app
COPY . /app

# Set environment variable for Flask (optional, if still using flask run)
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.build_app:app", "--reload"]



