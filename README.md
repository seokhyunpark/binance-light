# BinanceLight

This is a lightweight Python wrapper for interacting with the [Binance API](https://github.com/binance/binance-spot-api-docs), providing essential functionalities for trading. It is designed for simplicity and ease of use, making it perfect for users who only need basic trading operations without the complexity of a full-fledged library.

## Installation
To use BinanceLight, install the required package [Binance Public API Connector Python](https://github.com/binance/binance-connector-python) using pip:
```bash
pip install binance-connector
```

## Quick Start
Usage examples:
```python
import binancelight

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

client = binancelight.BinanceLight(api_key, api_secret)

price = client.get_ticker_price("BTCUSDT")
print(price)

orderbook = client.get_orderbook("BTCUSDT")
print(orderbook['bids'])
print(orderbook['asks'])

balances = client.get_balances()
print(balances)

buy = client.buy_limit_maker(symbol="BTCUSDT", quantity=1, price=60000)
print(buy)

sell = client.sell_limit_maker(symbol="BTCUSDT", quantity=1, price=120000)
print(sell)

order_id = buy['orderId']
order = client.get_order(symbol="BTCUSDT", order_id=order_id)
print(order)

order_id = sell['orderId']
cancel = client.cancel_order(symbol="BTCUSDT", order_id=order_id)
print(cancel)
```

## Error Logging
All errors encountered while using this library are automatically logged in a [filename].log file.  
The log entries include the date, time, error level, and error message. This ensures that any issues can be tracked and debugged effectively.

binancelight.log examples:
```python
[2024-09-01 04:50:31.111] ERROR (buy_limit_maker) ClientError: (400, -2010, 'Order would immediately match and take.', {'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': '62', 'Connection': 'keep-alive', 'Date': 'Sat, 31 Aug 2024 19:50:31 GMT', 'Server': 'nginx', 'x-mbx-uuid': '7e655 ...
```
```python
[2024-09-01 04:50:31.161] ERROR (sell_limit_maker) ClientError: (400, -2010, 'Account has insufficient balance for requested action.', {'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': '77', 'Connection': 'keep-alive', 'Date': 'Sat, 31 Aug 2024 19:50:31 GMT', 'Server': 'nginx', 'x-mbx-uuid': '42136 ...
```
