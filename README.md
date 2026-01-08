Bajaj Broking – Trading API Wrapper SDK (Simulation)
Overview

This project is a simplified trading backend with a Python wrapper SDK, built to simulate core workflows of an online stock broking platform.
It focuses on API design, trading concepts, and clean abstraction, not real market connectivity.

Features

View tradable instruments

Place BUY / SELL orders (MARKET / LIMIT)

Check order status

View executed trades

View portfolio holdings

Python wrapper SDK to abstract REST APIs

In-memory + JSON-based persistence

Basic validation and logging

Swagger (OpenAPI) documentation

Unit tests for core flows

Tech Stack

Backend: Python, FastAPI

SDK: Python (requests)

Storage: In-memory + JSON files

Testing: pytest

How to Run
1. Install dependencies
pip install -r requirements.txt

2. Start the backend
python -m uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

Using the Wrapper SDK
Example usage
from wrapper import Trader

trader = Trader()

print(trader.instruments())

order = trader.place("TCS", "BUY", "MARKET", 10)
print(order)

print(trader.portfolio())


Run:

python wrapper_test.py

Running Tests
pytest

Design Notes

Orders are executed immediately by design, so NEW and CANCELLED states are intentionally omitted.

MARKET orders default to last traded price for portfolio calculation.

Negative holdings are prevented (no short selling).

Authentication is mocked using a single hardcoded user.

Assumptions

Single user system

No real exchange integration

Simplified execution logic

Focus on correctness and clarity over complexity

Conclusion

This project demonstrates clean REST API design, basic trading domain understanding, and a wrapper SDK abstraction suitable for client integration, aligned with the assignment requirements.
