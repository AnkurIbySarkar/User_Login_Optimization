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

lint:
	docker-compose exec app flake8 app tests

format:
	docker-compose exec app black .