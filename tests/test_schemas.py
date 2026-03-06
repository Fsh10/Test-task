"""Тесты для Pydantic-схем."""
import pytest
from pydantic import ValidationError

from app.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
    ProvidersResponse,
    TariffResponse,
)


class TestCreatePaymentRequest:
    def test_valid_request(self):
        req = CreatePaymentRequest(
            tariff_id="1_month",
            user_id=1,
            method="sbp",
            provider="provider1",
        )
        assert req.tariff_id == "1_month"
        assert req.user_id == 1
        assert req.method == "sbp"
        assert req.provider == "provider1"

    def test_rejects_zero_user_id(self):
        with pytest.raises(ValidationError):
            CreatePaymentRequest(
                tariff_id="1_month",
                user_id=0,
                method="sbp",
                provider="provider1",
            )

    def test_rejects_negative_user_id(self):
        with pytest.raises(ValidationError):
            CreatePaymentRequest(
                tariff_id="1_month",
                user_id=-1,
                method="sbp",
                provider="provider1",
            )


class TestPaymentResponse:
    def test_creates_response(self):
        resp = PaymentResponse(payment_url="https://example.com/pay")
        assert resp.payment_url == "https://example.com/pay"


class TestTariffResponse:
    def test_creates_tariff_response(self):
        resp = TariffResponse(
            id="1_month",
            amount=199,
            description="Подписка 1 месяц",
            months=1,
        )
        assert resp.id == "1_month"
        assert resp.amount == 199


class TestProvidersResponse:
    def test_creates_providers_response(self):
        resp = ProvidersResponse(
            providers=["provider1", "provider2"],
            methods=["sbp", "card"],
        )
        assert resp.providers == ["provider1", "provider2"]
        assert resp.methods == ["sbp", "card"]
