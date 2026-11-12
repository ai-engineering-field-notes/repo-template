"""The failure, reproduced. Replace this demo with your own."""


def apply_discount(price_cents: int, percent: int) -> int:
    return price_cents - price_cents * percent // 100 if percent <= 100 else 0
