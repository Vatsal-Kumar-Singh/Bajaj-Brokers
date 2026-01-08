import json
import os

USER_ID = "demo_user"
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

ORDERS_FILE = os.path.join(DATA_DIR, "orders.json")
TRADES_FILE = os.path.join(DATA_DIR, "trades.json")
PORTFOLIO_FILE = os.path.join(DATA_DIR, "portfolio.json")

instruments = [
    {"symbol": "TCS", "exchange": "NSE", "IT": "EQ", "lastTradedPrice": 4200},
    {"symbol": "INFY", "exchange": "NSE", "IT": "EQ", "lastTradedPrice": 6900},
]

def load(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)
def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

orders = load(ORDERS_FILE, {})
trades = load(TRADES_FILE, [])
portfolio = load(PORTFOLIO_FILE, {})

def save_orders():
    save(ORDERS_FILE, orders)
def save_trades():
    save(TRADES_FILE, trades)
def save_portfolio():
    save(PORTFOLIO_FILE, portfolio)
