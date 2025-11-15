.PHONY: help install install-dev run test lint format clean docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install       - Install production dependencies"
	@echo "  make install-dev   - Install all dependencies including dev tools"
	@echo "  make run           - Run the Flask application"
	@echo "  make test          - Run tests with coverage"
	@echo "  make lint          - Run linters (flake8, mypy)"
	@echo "  make format        - Format code with black and isort"
	@echo "  make clean         - Remove cache and temporary files"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run application in Docker"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

run:
	python run.py

test:
	pytest --cov=app --cov-report=html --cov-report=term-missing

lint:
	flake8 app/ tests/
	mypy app/

format:
	black app/ tests/ config/
	isort app/ tests/ config/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build

docker-build:
	docker build -t flask-app:latest .

docker-run:
	docker-compose up --build
