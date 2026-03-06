"""Pydantic-схемы для API платежей."""
from pydantic import BaseModel, Field


class CreatePaymentRequest(BaseModel):
    """Запрос на создание платежа."""
    tariff_id: str = Field(..., description="Идентификатор тарифа: 1_month, 6_months, 1_year")
    user_id: int = Field(..., gt=0, description="ID пользователя")
    method: str = Field(..., description="Метод оплаты: sbp или card")
    provider: str = Field(..., description="Платёжный провайдер: provider1, provider2 и т.д.")


class PaymentResponse(BaseModel):
    """Ответ с платёжной ссылкой."""
    payment_url: str = Field(..., description="Ссылка для оплаты")


class TariffResponse(BaseModel):
    """Данные тарифа."""
    id: str
    amount: int
    description: str
    months: int


class ProvidersResponse(BaseModel):
    """Список провайдеров и методов оплаты."""
    providers: list[str]
    methods: list[str]
