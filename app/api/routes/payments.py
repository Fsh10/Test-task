"""API-эндпоинты для платежей и тарифов."""
from fastapi import APIRouter, HTTPException

from app.domain.providers import get_providers_and_methods
from app.domain.tariffs import get_all_tariffs
from app.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
    ProvidersResponse,
    TariffResponse,
)
from app.services.payment_service import PaymentCreationError, create_payment

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("/create", response_model=PaymentResponse)
def create_payment_endpoint(request: CreatePaymentRequest):
    """Создаёт платёж и возвращает платёжную ссылку."""
    try:
        payment_url = create_payment(
            tariff_id=request.tariff_id,
            user_id=request.user_id,
            method=request.method,
            provider=request.provider,
        )
        return PaymentResponse(payment_url=payment_url)
    except PaymentCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))


tariffs_router = APIRouter(tags=["tariffs"])


@tariffs_router.get("/tariffs", response_model=list[TariffResponse])
def list_tariffs():
    """Возвращает список доступных тарифов."""
    return [TariffResponse(**t) for t in get_all_tariffs()]


providers_router = APIRouter(tags=["providers"])


@providers_router.get("/providers", response_model=ProvidersResponse)
def list_providers():
    """Возвращает список провайдеров и методов оплаты для фронтенда."""
    return ProvidersResponse(**get_providers_and_methods())
