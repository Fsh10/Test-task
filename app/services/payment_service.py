"""Сервис создания платежей с валидацией."""
from payment_service import PaymentService as PaymentGateway

from app.domain.providers import is_method_valid, is_provider_valid
from app.domain.tariffs import get_tariff


class PaymentCreationError(Exception):
    """Ошибка при создании платежа (невалидные параметры)."""
    pass


def create_payment(
    tariff_id: str,
    user_id: int,
    method: str,
    provider: str,
) -> str:
    """
    Создаёт платёж с валидацией параметров.
    Возвращает платёжную ссылку.
    """
    tariff = get_tariff(tariff_id)
    if tariff is None:
        raise PaymentCreationError(f"Тариф '{tariff_id}' не найден")

    if not is_method_valid(method):
        raise PaymentCreationError(
            f"Метод оплаты '{method}' не поддерживается. "
            f"Доступные методы: sbp, card"
        )

    if not is_provider_valid(provider):
        raise PaymentCreationError(
            f"Провайдер '{provider}' не зарегистрирован"
        )

    payment_url = PaymentGateway.make_new_payment(
        amount=tariff["amount"],
        description=tariff["description"],
        user_id=user_id,
        method=method,
        provider=provider,
    )
    return payment_url
