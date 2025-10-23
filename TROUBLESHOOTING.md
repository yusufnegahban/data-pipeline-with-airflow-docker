# 🧩 Troubleshooting Guide

This document summarizes common errors and quick fixes encountered during the Airflow, Docker, and PostgreSQL setup for the book data pipeline project.

---

## 🌀 Errors Related to Airflow

### 1️⃣ Airflow UI Not Loading – localhost refused to connect
**Cause Summary:**  
- Webserver container not running or crashed  
- Port 8080 already in use or blocked by firewall  

**Fix Steps:**  
```bash
docker ps
docker-compose up -d
# If still blocked, change port in docker-compose.yml:
ports:
  - "8501:8080"
# Access UI at:
http://localhost:8501
```
**Funny Analogy:** Throwing a party but forgetting to unlock the door — everyone’s waiting outside 🕺🚪

---

### 2️⃣ DAG ImportError / Module Not Found
**Cause Summary:**  
- DAG file not in `/opt/airflow/dags`  
- Python module missing `__init__.py` or wrong path  

**Fix Steps:**  
```bash
docker exec -it airflow_project-airflow-scheduler-1 bash
cd /opt/airflow/dags && ls
```
Ensure all DAGs are properly placed with correct imports.

**Funny Analogy:** Like giving Airflow a recipe but leaving it in the wrong kitchen drawer 🍳🔎

---

### 3️⃣ AttributeError: module … has no attribute …
**Cause Summary:**  
- Function name in DAG doesn’t exist in imported module  
- Typos or refactoring left function undefined  

**Fix Steps:**  
Define the missing function or update the DAG to match the correct function.

**Funny Analogy:** Like shouting “Hey Alex!” in a room where nobody is named Alex 🤐🙋

---

### 4️⃣ AirflowNotFoundException: The conn_id postgres_default isn't defined
**Cause Summary:**  
- DAG expects a PostgreSQL connection not defined in Airflow  

**Fix Steps:**  
1. Open Airflow UI → Admin → Connections → + Add  
2. Fill in the following:  
   - Conn Id: `postgres_default`  
   - Conn Type: `Postgres`  
   - Host: `postgres`  
   - Schema: `airflow`  
   - Login: `airflow`  
   - Password: `securepass123`  
   - Port: `5432`  

**Funny Analogy:** Asking Airflow to call “Postgres” but forgetting the phone number 📞🤷

---

## 🐳 Errors Related to Docker & PostgreSQL

### 5️⃣ PostgreSQL: column “author” does not exist
**Cause Summary:**  
- Schema mismatch between DAG and DB  

**Fix Steps:**  
```bash
docker exec -it airflow_project-postgres-1 psql -U airflow -d airflow
\d books
ALTER TABLE books ADD COLUMN author TEXT;
ALTER TABLE books ADD COLUMN published_date DATE;
docker-compose restart
```
**Funny Analogy:** You tried to write “Author” on a card but there’s no “Author” line yet 📝

---

### 6️⃣ PostgreSQL ON CONFLICT Error
**Cause Summary:**  
- `ON CONFLICT` used without a unique constraint  

**Fix Steps:**  
```bash
docker exec -it airflow_project-postgres-1   psql -U airflow -d airflow   -c "ALTER TABLE books ADD CONSTRAINT unique_isbn UNIQUE (isbn);"
```
**Funny Analogy:** Telling a bouncer not to let duplicates in — but never defining who’s a duplicate 🕺

---

### 7️⃣ Password / Authentication Failed for user “airflow”
**Cause Summary:**  
- Password mismatch between Airflow and PostgreSQL  

**Fix Steps:**  
```bash
docker exec -it airflow_project-postgres-1 psql -U airflow -d airflow
ALTER USER airflow WITH PASSWORD 'securepass123';
```
Update environment variable in `docker-compose.yml` and restart containers.

**Funny Analogy:** Changed the lock but forgot the new key 🔑🚪

---

### 8️⃣ Clearing Old DAG Runs / XComs
**Cause Summary:**  
- Old runs cause conflicts after code fixes  

**Fix Steps:**  
```bash
docker exec -it airflow_project-airflow-scheduler-1   airflow dags clear books_pipeline --yes
docker exec -it airflow_project-airflow-scheduler-1   airflow tasks clear books_pipeline extract_books --yes
docker compose restart airflow-scheduler
```
**Funny Analogy:** Like running a new experiment in a dirty beaker — clean it first 🧪🧼

---

## 🐍 Python & Maintenance Errors

### 9️⃣ Checking Task Logs Inside Container
**Fix Steps:**  
```bash
docker exec -it airflow_project-airflow-scheduler-1   airflow tasks logs books_pipeline extract_books <run_id>
```
**Funny Analogy:** Like opening the black box of a plane to see what went wrong ✈️📦

---

### 🔟 Quick PostgreSQL Access in Docker
**Fix Steps:**  
```bash
docker exec -it airflow_project-postgres-1 psql -U airflow -d airflow
\d books
SELECT * FROM books LIMIT 10;
```
**Funny Analogy:** Like walking into the kitchen yourself to taste the soup 🥣👨‍🍳

---

### 1️⃣1️⃣ Test Port Access (PowerShell)
**Fix Steps:**  
```bash
Test-NetConnection -ComputerName localhost -Port 5432
```
**Funny Analogy:** Knocking on someone’s door to see if they’re home 🚪👋

---

### 1️⃣2️⃣ Resetting / Restarting Airflow Quickly
**Fix Steps:**  
```bash
docker-compose down
docker-compose up -d
docker ps
```
**Funny Analogy:** Like turning your computer off and on — it works more often than you’d think 💻🔄
