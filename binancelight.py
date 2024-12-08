from binance.spot import Spot
from inspect import stack
from logger import get_logger

log = get_logger("binancelight")


def _handle_exception(e):
    # print(f"status code: {e.status_code}")
    # print(f"error code: {e.error_code}")
    # print(f"error message: {e.error_message}")
    # print(f"header: {e.header}")
    # print(f"error data: {e.error_data}")
    log.error(f"({stack()[1].function}) {e.__class__.__name__}: {e}")
    return None


class BinanceLight:
    def __init__(self, api_key, api_secret):
        self.private = Spot(api_key, api_secret)
        self.public = Spot()

    def get_ticker_price(self, symbol):
        try:
            ticker_price = self.public.ticker_price(symbol=symbol)
            price = float(ticker_price['price'])
            return price
        except Exception as e:
            return _handle_exception(e)

    def get_orderbook(self, symbol, limit):
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

    def buy_limit_maker(self, symbol, quantity, price):
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

    def sell_limit_maker(self, symbol, quantity, price):
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

    def get_order(self, symbol, order_id):
        try:
            order = self.private.get_order(
                symbol=symbol,
                orderId=order_id
            )
            return order
        except Exception as e:
            return _handle_exception(e)

    def get_open_orders(self, symbol):
        try:
            orders = self.private.get_open_orders(symbol=symbol)
            return orders
        except Exception as e:
            return _handle_exception(e)

    def cancel_order(self, symbol, order_id):
        try:
            order = self.private.cancel_order(
                symbol=symbol,
                orderId=order_id
            )
            return order
        except Exception as e:
            return _handle_exception(e)

    def cancel_open_orders(self, symbol):
        try:
            order = self.private.cancel_open_orders(symbol=symbol)
            return order
        except Exception as e:
            return _handle_exception(e)

    def get_exchange_info(self, symbol):
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

    def renew_listen_key(self, listen_key):
        try:
            listen_key = self.private.renew_listen_key(listen_key)
            return listen_key
        except Exception as e:
            return _handle_exception(e)

    def get_klines(self, symbol, interval, limit):
        try:
            klines = self.public.klines(symbol=symbol, interval=interval, limit=limit)
            return klines
        except Exception as e:
            return _handle_exception(e)

    def ticker_24hr(self, symbol=None):
        try:
            if symbol is None:
                return self.public.ticker_24hr()
            else:
                return self.public.ticker_24hr(symbol=symbol)
        except Exception as e:
            return _handle_exception(e)
