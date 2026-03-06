"""Тесты для API эндпоинтов."""
import pytest
from fastapi.testclient import TestClient


class TestCreatePaymentEndpoint:
    def test_creates_payment_success(self, client: TestClient):
        response = client.post(
            "/payments/create",
            json={
                "tariff_id": "1_month",
                "user_id": 1,
                "method": "sbp",
                "provider": "provider1",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert "payment_url" in data
        assert "https://payment_link.com" in data["payment_url"]

    def test_returns_400_for_invalid_tariff(self, client: TestClient):
        response = client.post(
            "/payments/create",
            json={
                "tariff_id": "invalid",
                "user_id": 1,
                "method": "sbp",
                "provider": "provider1",
            },
        )
        assert response.status_code == 400
        assert "Тариф" in response.json()["detail"]

    def test_returns_400_for_invalid_method(self, client: TestClient):
        response = client.post(
            "/payments/create",
            json={
                "tariff_id": "1_month",
                "user_id": 1,
                "method": "crypto",
                "provider": "provider1",
            },
        )
        assert response.status_code == 400
        assert "Метод" in response.json()["detail"]

    def test_returns_400_for_invalid_provider(self, client: TestClient):
        response = client.post(
            "/payments/create",
            json={
                "tariff_id": "1_month",
                "user_id": 1,
                "method": "sbp",
                "provider": "unknown",
            },
        )
        assert response.status_code == 400
        assert "Провайдер" in response.json()["detail"]

    def test_returns_422_for_invalid_user_id(self, client: TestClient):
        response = client.post(
            "/payments/create",
            json={
                "tariff_id": "1_month",
                "user_id": 0,
                "method": "sbp",
                "provider": "provider1",
            },
        )
        assert response.status_code == 422


class TestListTariffsEndpoint:
    def test_returns_all_tariffs(self, client: TestClient):
        response = client.get("/tariffs")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3
        ids = {t["id"] for t in data}
        assert ids == {"1_month", "6_months", "1_year"}

    def test_tariff_has_required_fields(self, client: TestClient):
        response = client.get("/tariffs")
        tariff = response.json()[0]
        assert "id" in tariff
        assert "amount" in tariff
        assert "description" in tariff
        assert "months" in tariff


class TestListProvidersEndpoint:
    def test_returns_providers_and_methods(self, client: TestClient):
        response = client.get("/providers")
        assert response.status_code == 200
        data = response.json()
        assert "providers" in data
        assert "methods" in data
        assert "provider1" in data["providers"]
        assert "provider2" in data["providers"]
        assert "sbp" in data["methods"]
        assert "card" in data["methods"]
