from binance.spot import Spot
from inspect import stack
from logger import Logger

logger = Logger("binancelight")


def _handle_exception(e):
    # print(f"status code: {e.status_code}")
    # print(f"error code: {e.error_code}")
    # print(f"error message: {e.error_message}")
    # print(f"header: {e.header}")
    # print(f"error data: {e.error_data}")
    logger.error(f"({stack()[1].function}) {e.__class__.__name__}: {e}")
    return None


class BinanceLight:
    def __init__(self, api_key: str, api_secret: str):
        self.private = Spot(api_key, api_secret)
        self.public = Spot()

    def get_ticker_price(self, symbol: str):
        try:
            ticker_price = self.public.ticker_price(symbol=symbol)
            price = float(ticker_price['price'])
            return price
        except Exception as e:
            return _handle_exception(e)

    def get_orderbook(self, symbol: str, limit: int):
        try:
            depth = self.public.depth(symbol=symbol, limit=limit)
            orderbook = {'bids': depth['bids'], 'asks': depth['asks']}
            return orderbook
        except Exception as e:
            return _handle_exception(e)

    def get_balances(self):
        try:
            account = self.private.account(omitZeroBalances="true")
            balances = account['balances']
            return balances
        except Exception as e:
            return _handle_exception(e)

    def get_balance(self, asset: str):
        try:
            balances = self.get_balances()
            for balance in balances:
                if balance['asset'] == asset:
                    return float(balance['free'])
            return 0
        except Exception as e:
            return _handle_exception(e)

    def buy_limit_maker(self, symbol: str, quantity: float, price: float):
        try:
            buy = self.private.new_order(
                symbol=symbol,
                side='BUY',
                type='LIMIT_MAKER',
                quantity=quantity,
                price=price
            )
            return buy
        except Exception as e:
            return _handle_exception(e)

    def sell_limit_maker(self, symbol: str, quantity: float, price: float):
        try:
            sell = self.private.new_order(
                symbol=symbol,
                side='SELL',
                type='LIMIT_MAKER',
                quantity=quantity,
                price=price
            )
            return sell
        except Exception as e:
            return _handle_exception(e)

    def get_order(self, symbol: str, order_id: int):
        try:
            order = self.private.get_order(
                symbol=symbol,
                orderId=order_id
            )
            return order
        except Exception as e:
            return _handle_exception(e)

    def get_open_orders(self, symbol: str):
        try:
            orders = self.private.get_open_orders(symbol=symbol)
            return orders
        except Exception as e:
            return _handle_exception(e)

    def cancel_order(self, symbol: str, order_id: int):
        try:
            order = self.private.cancel_order(
                symbol=symbol,
                orderId=order_id
            )
            return order
        except Exception as e:
            return _handle_exception(e)

    def get_exchange_info(self, symbol: str):
        try:
            exchange_info = self.public.exchange_info(symbol=symbol)
            return exchange_info
        except Exception as e:
            return _handle_exception(e)

    def get_rate_order_limit(self):
        try:
            rate_limit = self.private.get_order_rate_limit()
            return rate_limit
        except Exception as e:
            return _handle_exception(e)

    def get_new_listen_key(self):
        try:
            listen_key = self.private.new_listen_key()
            return listen_key
        except Exception as e:
            return _handle_exception(e)

    def renew_listen_key(self, listen_key: str):
        try:
            listen_key = self.private.renew_listen_key(listen_key)
            return listen_key
        except Exception as e:
            return _handle_exception(e)

    def get_klines(self, symbol: str, interval: str, limit: int):
        try:
            klines = self.public.klines(symbol=symbol, interval=interval, limit=limit)
            return klines
        except Exception as e:
            return _handle_exception(e)
