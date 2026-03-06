.PHONY: run run-dev test build docker-build docker-run help

# Default target
help:
	@echo "Доступные команды:"
	@echo "  make run        - Запуск приложения"
	@echo "  make run-dev    - Запуск с hot-reload"
	@echo "  make test       - Запуск тестов"
	@echo "  make build      - Сборка Docker-образа"
	@echo "  make docker-run - Запуск контейнера"

# Запуск приложения
run:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8000

# Запуск с hot-reload для разработки
run-dev:
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Запуск тестов
test:
	uv run pytest tests/ -v

# Сборка Docker-образа
build:
	docker build -t payment-api:latest .

# Запуск Docker-контейнера
docker-run: build
	docker run -p 8000:8000 payment-api:latest
