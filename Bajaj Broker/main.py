from fastapi import FastAPI, HTTPException
import uuid
import logging
from model import OrderRequest
from store import instruments, orders, trades, portfolio, USER_ID, save_orders
from execution import execute_order

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Bajaj Broking",
    description="View Instruments, Place Orders, View Trades and Portfolio",
)

@app.get("/instruments", tags=["Instruments"])
def get_instruments():
    logger.info("Getting instruments")
    return instruments
@app.post("/orders/place", tags=["Orders"])
def place(order: OrderRequest):
    logger.info(f"Company: {order.symbol}")
    symbols = [i["symbol"] for i in instruments]
    if order.symbol not in symbols:
        raise HTTPException(400, "Invalid trading symbol")
    if order.side not in ["BUY", "SELL"]:
        raise HTTPException(400, "Invalid order side")
    if order.quantity <= 0:
        raise HTTPException(400, "Quantity must be greater than 0")
    if order.orderType == "LIMIT":
        if order.price is None or order.price <= 0:
            raise HTTPException(400, "Valid price required for LIMIT order")
    order_id = str(uuid.uuid4())
    new_order = {
        "orderId": order_id,
        "symbol": order.symbol,
        "side": order.side,
        "orderType": order.orderType,
        "quantity": order.quantity,
        "price": order.price,
        "status": "PLACED",
        "userId": USER_ID
    }
    orders[order_id] = new_order
    save_orders()
    execute_order(new_order)
    return {"orderId": order_id, "status": new_order["status"]}

@app.get("/orders/status/{order_id}", tags=["Orders"])
def status(order_id: str):
    if order_id not in orders:
        raise HTTPException(404, "Order not found")
    return orders[order_id]

@app.get("/trades", tags=["Trades"])
def gettrades():
    return trades

@app.get("/portfolio", tags=["Portfolio"])
def get_portfolio():
    if not portfolio:
        return {"message": "No holdings yet"}
    result = []
    for symbol, data in portfolio.items():
        avg_price = data["averagePrice"] if data["averagePrice"] is not None else 0
        result.append({
            "symbol": symbol,
            "quantity": data["quantity"],
            "averagePrice": avg_price,
            "currentValue": data["quantity"] * avg_price
        })
    return result

