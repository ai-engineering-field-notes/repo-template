# Example demo (delete when you add the first real one)

## Problem

A discount function accepts a negative percentage and raises the price instead.

## Business pain

Customers are overcharged by a bug that looks like a discount.

## Fix

`after/discount.py` rejects percentages outside 0 to 100.

## Proof

`tests/test_example.py` shows the overcharge in `before/` and the rejection in `after/`.

```
uv run pytest demos/00-example
```
