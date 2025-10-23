# ===============================
# Airflow & Docker Configuration
# ===============================
AIRFLOW_IMAGE_NAME=apache/airflow:2.9.1
AIRFLOW_PROJ_DIR=.
AIRFLOW_UID=50000

# ===============================
# PostgreSQL Configuration
# ===============================
POSTGRES_USER=airflow
POSTGRES_PASSWORD=your_password_here
POSTGRES_DB=airflow
POSTGRES_HOST=postgres

# ===============================
# Airflow Database Connection
# ===============================
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:your_password_here@postgres:5432/airflow

# ===============================
# Celery & Redis Configuration
# ===============================
AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://airflow:your_password_here@postgres/airflow
AIRFLOW__CELERY__BROKER_URL=redis://:@redis:6379/0

# ===============================
# Airflow Core Settings
# ===============================
AIRFLOW__CORE__FERNET_KEY=your_fernet_key_here
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=true
AIRFLOW__CORE__LOAD_EXAMPLES=false
AIRFLOW__API__AUTH_BACKENDS=airflow.api.auth.backend.basic_auth,airflow.api.auth.backend.session
AIRFLOW__SCHEDULER__ENABLE_HEALTH_CHECK=true
