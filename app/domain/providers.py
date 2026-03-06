"""Реестр платёжных провайдеров и методов оплаты."""

# Список зарегистрированных провайдеров. Для добавления нового — добавить имя в множество.
PROVIDERS = {"provider1", "provider2"}

# Поддерживаемые методы оплаты (СБП, банковская карта)
PAYMENT_METHODS = {"sbp", "card"}


def is_provider_valid(provider: str) -> bool:
    """Проверяет, зарегистрирован ли провайдер."""
    return provider in PROVIDERS


def is_method_valid(method: str) -> bool:
    """Проверяет, поддерживается ли метод оплаты."""
    return method in PAYMENT_METHODS


def get_providers_and_methods() -> dict:
    """Возвращает список провайдеров и методов для фронтенда."""
    return {
        "providers": list(PROVIDERS),
        "methods": list(PAYMENT_METHODS),
    }
