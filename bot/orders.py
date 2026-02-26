import logging
from bot.client import send_signed_request


def place_market_order(symbol, side, quantity):

    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    }

    order = send_signed_request("POST", "/fapi/v1/order", params)

    logging.info(order)

    return order


def place_limit_order(symbol, side, quantity, price):

    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC"
    }

    order = send_signed_request("POST", "/fapi/v1/order", params)

    logging.info(order)

    return order