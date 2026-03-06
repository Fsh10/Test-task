"""Тесты для app.domain.tariffs."""
import pytest

from app.domain.tariffs import TARIFFS, get_all_tariffs, get_tariff


class TestGetTariff:
    def test_returns_tariff_for_valid_id(self):
        result = get_tariff("1_month")
        assert result == {"amount": 199, "description": "Подписка 1 месяц", "months": 1}

    def test_returns_tariff_6_months(self):
        result = get_tariff("6_months")
        assert result == {"amount": 849, "description": "Подписка 6 месяцев", "months": 6}

    def test_returns_tariff_1_year(self):
        result = get_tariff("1_year")
        assert result == {"amount": 1699, "description": "Подписка 1 год", "months": 12}

    def test_returns_none_for_invalid_id(self):
        assert get_tariff("invalid") is None

    def test_returns_none_for_empty_string(self):
        assert get_tariff("") is None


class TestGetAllTariffs:
    def test_returns_all_tariffs_with_ids(self):
        result = get_all_tariffs()
        assert len(result) == 3
        ids = {t["id"] for t in result}
        assert ids == {"1_month", "6_months", "1_year"}

    def test_each_tariff_has_required_fields(self):
        result = get_all_tariffs()
        for tariff in result:
            assert "id" in tariff
            assert "amount" in tariff
            assert "description" in tariff
            assert "months" in tariff

    def test_amounts_match_tariffs_config(self):
        result = get_all_tariffs()
        amounts = {t["id"]: t["amount"] for t in result}
        assert amounts["1_month"] == 199
        assert amounts["6_months"] == 849
        assert amounts["1_year"] == 1699
