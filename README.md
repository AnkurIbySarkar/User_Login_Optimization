# 🚀 User Login Optimization

A mini-project to benchmark different strategies for checking if a user exists in a PostgreSQL database. It compares raw SQL queries, Python logic, and Redis-based caching, with an interactive Streamlit UI for insights.

---

## ✅ Features

- 🔍 Brute-force vs Redis-cached lookup
- 📊 Streamlit UI to benchmark performance
- 🔁 Batch testing to compute average lookup time
- 🔄 Redis cache metrics (hit/miss tracking)
- ♻️ Live cache + metric reset
- 🐳 Fully Dockerized
- 🧪 CI-integrated test suite

---

## 🧰 Tech Stack

| Layer           | Tech                        |
|----------------|-----------------------------|
| Backend API     | FastAPI                    |
| Database        | PostgreSQL (via Docker)     |
| Cache           | Redis                       |
| UI              | Streamlit                   |
| Tests           | Pytest, Coverage            |
| CI/CD           | GitHub Actions              |
| DevOps          | Docker Compose, Makefile    |

---

## 📁 Project Structure

├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── queries/
│ │ ├── brute_force.py
│ │ └── redis_cached.py
│ ├── routes/
│ │ ├── user_check.py
│ │ └── metrics.py
│ ├── metrics/
│ │ └── cache_tracker.py
│ ├── cache/
│ └── redis_client.py
│
├── benchmark/
│ └── compare.py
│
├── tests/
│ ├── conftest.py
│ ├── test_api.py
│ ├── test_brute_force.py
│ └── test_redis_cached.py
│
├── streamlit_app.py
├── docker-compose.yml
├── Makefile
└── requirements.txt

yaml
Copy
Edit

---

## 🚀 Run Locally

### 1. Clone & Setup

```bash
git clone https://github.com/yourname/user-login-optimization.git
cd user-login-optimization
```

### 2. Start the Services

```bash
make up
```

This spins up:

- FastAPI backend (http://localhost:8000)

- Redis (localhost:6379)

- PostgreSQL (localhost:5432)

- Streamlit UI (http://localhost:8501)

### 3. Seed Test Data

```bash
make seed-test
```

### 4. Launch UI
Visit 👉 http://localhost:8501 to use the Streamlit dashboard.

🧪 Testing & Linting
bash
Copy
Edit
make test         # Run all Pytest tests
make coverage     # Check code coverage
make lint         # Lint with flake8
make format       # Format with Black

⚙️ Makefile Commands

```bash
# Start the Docker stack
up:
	docker-compose up --build -d

# Tear down everything
down:
	docker-compose down -v

# Seed full dataset (1M+ users)
seed:
	docker-compose exec app python app/seed.py

# Seed small test dataset (for dev or CI parity)
seed-test:
	docker-compose exec app python tests/seed_test_db.py

# Run tests inside the container
test:
	docker-compose exec app pytest
```

🧪 CI/CD
- GitHub Actions is used for:

- Setup & dependency caching

- Code linting via flake8

- Seeding PostgreSQL test data

- Running pytest with coverage

- Boot-checking Streamlit service