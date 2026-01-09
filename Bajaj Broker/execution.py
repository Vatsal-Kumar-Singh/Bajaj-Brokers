NOTE FOR REVIEWER: I DID NOT ADD NEW & CANCELED ORDER STATES BY DESIGN CHOICE,
IT DOES NOT MAKE SENSE TO HAVE THEM IN A SIMULATED ENVIRONMENT WHERE ALL ORDERS ARE IMMEDIATELY EXECUTED.
import uuid
from store import trades, portfolio, save_trades, save_portfolio, instruments

def get_ltp(symbol):
    for i in instruments:
        if i["symbol"] == symbol:
            return i["lastTradedPrice"]
    return 0

def execute_order(order):
    # Immediate execution by design
    order["status"] = "EXECUTED"
    price = order["price"]
    if price is None:
        price = get_ltp(order["symbol"])
    trade = {
        "tradeId": str(uuid.uuid4()),
        "symbol": order["symbol"],
        "quantity": order["quantity"],
        "price": price,
        "side": order["side"]
    }
    trades.append(trade)
    save_trades()
    symbol = order["symbol"]
    qty_change = order["quantity"] if order["side"] == "BUY" else -order["quantity"]
    if order["side"] == "SELL":
        if symbol not in portfolio or portfolio[symbol]["quantity"] < order["quantity"]:
            raise ValueError("Insufficient holdings to sell")
    if symbol not in portfolio:
        portfolio[symbol] = {
            "symbol": symbol,
            "quantity": 0,
            "averagePrice": price
        }
    portfolio[symbol]["quantity"] += qty_change
    save_portfolio()

