"""Тесты для app.domain.providers."""
import pytest

from app.domain.providers import (
    PAYMENT_METHODS,
    PROVIDERS,
    get_providers_and_methods,
    is_method_valid,
    is_provider_valid,
)


class TestIsProviderValid:
    def test_returns_true_for_provider1(self):
        assert is_provider_valid("provider1") is True

    def test_returns_true_for_provider2(self):
        assert is_provider_valid("provider2") is True

    def test_returns_false_for_unknown_provider(self):
        assert is_provider_valid("provider3") is False

    def test_returns_false_for_empty_string(self):
        assert is_provider_valid("") is False


class TestIsMethodValid:
    def test_returns_true_for_sbp(self):
        assert is_method_valid("sbp") is True

    def test_returns_true_for_card(self):
        assert is_method_valid("card") is True

    def test_returns_false_for_unknown_method(self):
        assert is_method_valid("crypto") is False

    def test_returns_false_for_empty_string(self):
        assert is_method_valid("") is False


class TestGetProvidersAndMethods:
    def test_returns_providers_list(self):
        result = get_providers_and_methods()
        assert "providers" in result
        assert set(result["providers"]) == PROVIDERS

    def test_returns_methods_list(self):
        result = get_providers_and_methods()
        assert "methods" in result
        assert set(result["methods"]) == PAYMENT_METHODS
