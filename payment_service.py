from urllib.parse import urlencode


class PaymentService:
    @classmethod
    def make_new_payment(
        cls,
        amount: int,
        description: str,
        user_id: int,
        method: str,
        provider: str,
    ) -> str:
        base_url = "https://payment_link.com"
        query_params = {
            "amount": amount,
            "desc": description,
        }
        return f"{base_url}?{urlencode(query_params)}"
