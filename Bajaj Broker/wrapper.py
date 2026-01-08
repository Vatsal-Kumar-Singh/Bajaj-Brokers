import requests

class Trader:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def get_instruments(self):
        return requests.get(f"{self.base_url}/instruments").json()

    def place(self, symbol, side, order_type, quantity, price=None):
        payload = {
            "symbol": symbol,
            "side": side,
            "orderType": order_type,
            "quantity": quantity,
            "price": price
        }
        return requests.post(f"{self.base_url}/orders/place", json=payload).json()

    def get_trades(self):
        return requests.get(f"{self.base_url}/trades").json()
    
    def get_portfolio(self):
        return requests.get(f"{self.base_url}/portfolio").json()