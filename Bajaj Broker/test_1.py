from fastapi.testclient import TestClient
from main import app

tester = TestClient(app)

def test_get_instruments():
    response = tester.get("/instruments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_place():
    response = tester.post("/orders/place", json={
        "symbol": "BajajAuto",
        "side": "BUY",
        "orderType": "MARKET",
        "quantity": 5
    })
    assert response.status_code == 200
    assert "orderId" in response.json()

