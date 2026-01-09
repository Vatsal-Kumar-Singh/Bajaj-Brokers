from wrapper import Trader

trader = Trader()

print(trader.get_instruments())

order = trader.place(
    symbol="BajajAuto",
    side="BUY",
    order_type="MARKET",
    quantity=10
)
print(order)

print(trader.get_portfolio())

