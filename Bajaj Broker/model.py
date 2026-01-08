from pydantic import BaseModel
from typing import Optional

class OrderRequest(BaseModel):
    symbol: str
    side: str        # BUY / SELL
    orderType: str   # MARKET / LIMIT
    quantity: int
    price: Optional[float] = None
