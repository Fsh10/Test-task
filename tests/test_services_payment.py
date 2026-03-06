"""Тесты для app.services.payment_service."""
import pytest

from app.services.payment_service import PaymentCreationError, create_payment


class TestCreatePaymentSuccess:
    def test_creates_payment_for_1_month_sbp_provider1(self):
        url = create_payment(
            tariff_id="1_month",
            user_id=1,
            method="sbp",
            provider="provider1",
        )
        assert "https://payment_link.com" in url
        assert "amount=199" in url
        assert "desc=" in url

    def test_creates_payment_for_6_months_card_provider2(self):
        url = create_payment(
            tariff_id="6_months",
            user_id=42,
            method="card",
            provider="provider2",
        )
        assert "amount=849" in url

    def test_creates_payment_for_1_year(self):
        url = create_payment(
            tariff_id="1_year",
            user_id=100,
            method="sbp",
            provider="provider1",
        )
        assert "amount=1699" in url


class TestCreatePaymentValidation:
    def test_raises_for_invalid_tariff(self):
        with pytest.raises(PaymentCreationError) as exc_info:
            create_payment(
                tariff_id="invalid_tariff",
                user_id=1,
                method="sbp",
                provider="provider1",
            )
        assert "Тариф 'invalid_tariff' не найден" in str(exc_info.value)

    def test_raises_for_invalid_method(self):
        with pytest.raises(PaymentCreationError) as exc_info:
            create_payment(
                tariff_id="1_month",
                user_id=1,
                method="crypto",
                provider="provider1",
            )
        assert "Метод оплаты 'crypto' не поддерживается" in str(exc_info.value)
        assert "sbp, card" in str(exc_info.value)

    def test_raises_for_invalid_provider(self):
        with pytest.raises(PaymentCreationError) as exc_info:
            create_payment(
                tariff_id="1_month",
                user_id=1,
                method="sbp",
                provider="unknown_provider",
            )
        assert "Провайдер 'unknown_provider' не зарегистрирован" in str(exc_info.value)
