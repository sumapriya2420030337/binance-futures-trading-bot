import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    side = validate_side(args.side)
    order_type = validate_order_type(args.type)

    print("\nOrder Request Summary")
    print("----------------------")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {args.quantity}")

    if order_type == "LIMIT":

        if not args.price:
            raise ValueError("LIMIT orders require --price")

        print(f"Price: {args.price}")

        order = place_limit_order(
            args.symbol,
            side,
            args.quantity,
            args.price
        )

    else:

        order = place_market_order(
            args.symbol,
            side,
            args.quantity
        )

    print("\nOrder Response")
    print("----------------------")

    if "orderId" in order:

        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order['executedQty']}")

        print("\nSUCCESS: Order placed!")

    else:

        print("API returned error:")
        if "code" in order:
             print(f"API Error {order['code']}: {order['msg']}")
        else:
            print(f"Order ID: {order['orderId']}")
            print(f"Status: {order['status']}")
            print(f"Executed Qty: {order['executedQty']}")

except Exception as e:

    print("\nERROR:", e)