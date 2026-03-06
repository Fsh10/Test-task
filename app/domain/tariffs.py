"""Реестр тарифов подписки."""

TARIFFS = {
    "1_month": {"amount": 199, "description": "Подписка 1 месяц", "months": 1},
    "6_months": {"amount": 849, "description": "Подписка 6 месяцев", "months": 6},
    "1_year": {"amount": 1699, "description": "Подписка 1 год", "months": 12},
}


def get_tariff(tariff_id: str) -> dict | None:
    """Возвращает данные тарифа по идентификатору."""
    return TARIFFS.get(tariff_id)


def get_all_tariffs() -> list[dict]:
    """Возвращает список всех тарифов."""
    return [
        {"id": tariff_id, **data}
        for tariff_id, data in TARIFFS.items()
    ]
