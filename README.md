# Payment API

FastAPI-приложение для создания платежей по тарифам подписки с поддержкой нескольких методов оплаты (СБП, карта) и платёжных провайдеров.

## Архитектура

Решение построено на реестрах тарифов и провайдеров. Бизнес-логика в сервисном слое валидирует параметры (тариф, метод, провайдер) и делегирует создание платёжной ссылки функции `make_new_payment`. Добавление нового тарифа или провайдера не требует изменения основной логики.

## Добавление платёжного провайдера

Добавьте имя провайдера в множество `PROVIDERS` в файле `app/domain/providers.py`:

```python
PROVIDERS = {"provider1", "provider2", "provider3"}  # новый провайдер
```

## Добавление тарифа

Добавьте запись в словарь `TARIFFS` в файле `app/domain/tariffs.py`:

```python
TARIFFS = {
    ...
    "2_years": {"amount": 2999, "description": "Подписка 2 года", "months": 24},
}
```

## Запуск проекта

Проект использует [uv](https://docs.astral.sh/uv/) в качестве менеджера зависимостей.

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Через Makefile:
```bash
make run       # запуск приложения
make run-dev   # запуск с hot-reload
make build     # сборка Docker-образа
make docker-run # сборка и запуск контейнера
```

API будет доступен по адресу http://127.0.0.1:8000. Документация — http://127.0.0.1:8000/docs.

## Тесты

```bash
uv run pytest tests/ -v
uv run pytest tests/ --cov=app --cov=payment_service --cov-report=term-missing
```

## Пример создания платежа (cURL)

```bash
curl -X POST "http://127.0.0.1:8000/payments/create" \
  -H "Content-Type: application/json" \
  -d '{"tariff_id": "1_month", "user_id": 1, "method": "sbp", "provider": "provider1"}'
```
