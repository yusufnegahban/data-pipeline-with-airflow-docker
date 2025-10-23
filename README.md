
# 📘 Dockerized Data Pipeline Project  

> A **simple yet complete data pipeline project** built with **Docker**, **Apache Airflow**, **PostgreSQL**, and **Python** — designed to demonstrate core concepts clearly for learners, technical managers, and recruiters.

---

## ⚙️ Project Overview  

This project shows how multiple services can work together inside Docker containers:  

- 🐍 **Python scripts** → e.g., `scraper.py`, `books_pipeline.py`  
- 🗄️ **Database** → PostgreSQL  
- 🔁 **Workflow orchestrator** → Apache Airflow  
- 📊 *(Optional)* **Visualization** → Apache Superset  

Everything runs seamlessly in containers, making it reproducible on any system with Docker installed.

---

## 🧩 Step-by-Step Execution  

### 1️⃣ Prepare Project Structure  
Organize your code and configuration into clean folders:
```
app/
analytics/
dags/
```

Each component (scraper, database, Airflow) lives in its own folder for clarity.

---

### 2️⃣ Write the Dockerfile  
Each service gets its own `Dockerfile` describing how to build and run it.

Example:
```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "scraper.py"]
```

---

### 3️⃣ Define Services in docker-compose.yml ❤️  
This is the heart of the project — it connects all containers together:

- **postgres** → database  
- **airflow-*** → Airflow scheduler, webserver, worker, triggerer  
- *(Optional)* **Flask or Scraper** service  

Then simply run:
```bash
docker compose up -d
```

---

### 4️⃣ Connect the Services  
- Airflow connects to PostgreSQL using a **Connection ID** (e.g., `postgres_default`).  
- The **DAG** (`books_pipeline.py`) triggers the scraper and stores results into PostgreSQL.  
- Superset (optional) can later visualize these results.

---

### 5️⃣ Test and Manage  
Everything runs inside containers, so you can test easily:  

- Access **Airflow UI** → check if DAGs are loaded and active.  
- Inspect **PostgreSQL** → confirm data insertion.  

---

## 📁 Project Structure  

```
.dockerignore
.env
.flaskenv
.gitignore
create_tables.py
docker-compose.yml
requirements.txt
run.py
README.md
```

### app/
```
api.py
build_app.py
models.py
scraper.py
Dockerfile
__init__.py
```

### analytics/
```
spark_postgres_analysis.py
max_salebook.py
test_pandas_pyarrow.py
```

### dags/
```
scraper_airflow.py
save_to_db.py
books_pipeline.py
```

---

## 🧠 Common Issues & Fixes  

| ⚠️ Problem | 💡 Solution | 🧩 Explanation |
|-------------|--------------|----------------|
| `ModuleNotFoundError: No module named 'scraper'` | Copy scraper files into the DAGs folder and fix import paths. | 📚 *“The books were hiding — we invited them into Airflow city.”* |
| DAG not visible in Airflow UI | Rename the DAG file correctly and clear cache. | 👀 *“The DAG was playing hide-and-seek — renaming made it wave hello.”* |
| `ModuleNotFoundError: No module named 'app'` | Move database/model logic into a standalone file like `models_airflow.py`. | 🏗️ *“The models were stuck in the Flask castle — now they live in Airflow.”* |
| `password authentication failed for user "postgres"` | Sync credentials with `.env` and `docker-compose.yml`. | 🔑 *“PostgreSQL finally accepted our right keys.”* |
| DAG execution error | Verify all containers are running and dependencies exist in the DAGs folder. | 🚀 *“The DAGs were sleeping — we woke them up by organizing their files.”* |

---

## 🧩 Technical Highlights  

- **PostgresHook** in Airflow handles PostgreSQL connections elegantly via `Connection ID`.  
- No hardcoded credentials — everything is securely managed by Airflow.  
- The `Book` model contains only essential fields:  
  ```python
  id, title, price, availability
  ```  
- `Base.metadata.create_all(bind=engine)` automatically creates tables if missing.  

---

## 🎯 Final Result  

✅ Fully containerized data pipeline  
✅ Portable across any system with Docker  
✅ Minimal, clean, and understandable codebase  
✅ Perfect for showing your understanding of **Docker**, **Airflow**, and **data engineering fundamentals**

---

## 💬 Why I Built This Project  

I built this project as a **practical learning journey** to understand how modern data pipelines work — from data extraction to storage, orchestration, and visualization — using real tools used by data engineers in production.  

My goal was **not just to make it work**, but to make it **clear, reproducible, and educational** — so anyone (even non-developers) can open the project, run one command, and see a complete data pipeline in action.  

Through this project, I learned how to:  
- 🧩 Structure services inside Docker containers  
- 🔁 Orchestrate workflows using Apache Airflow  
- 🗄️ Store and query data in PostgreSQL  
- ⚙️ Debug common container issues  
- 🧠 Keep everything simple, modular, and production-friendly  

This project reflects my **transition from a marketing professional to a data engineer**, showing my curiosity, persistence, and real understanding of how data flows through modern systems.  

> 🚀 I believe simplicity is the ultimate sophistication — and that’s exactly what this project represents.  
