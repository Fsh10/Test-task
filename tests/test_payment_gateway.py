"""Тесты для payment_service.PaymentService (make_new_payment)."""
from urllib.parse import parse_qs, urlparse

from payment_service import PaymentService


class TestMakeNewPayment:
    def test_returns_url_with_base(self):
        url = PaymentService.make_new_payment(
            amount=100,
            description="Test",
            user_id=1,
            method="sbp",
            provider="provider1",
        )
        assert url.startswith("https://payment_link.com")

    def test_url_contains_amount(self):
        url = PaymentService.make_new_payment(
            amount=199,
            description="Test",
            user_id=1,
            method="sbp",
            provider="provider1",
        )
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        assert params["amount"] == ["199"]

    def test_url_contains_description(self):
        url = PaymentService.make_new_payment(
            amount=100,
            description="Подписка 1 месяц",
            user_id=1,
            method="sbp",
            provider="provider1",
        )
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        assert "desc" in params
        assert "Подписка" in params["desc"][0]
