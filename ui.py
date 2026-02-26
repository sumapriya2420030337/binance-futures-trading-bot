from flask import Flask, render_template, request
from bot.orders import place_market_order, place_limit_order, place_stop_order
import requests

app = Flask(__name__)


def get_price(symbol):
    url = f"https://testnet.binancefuture.com/fapi/v1/ticker/price?symbol={symbol}"
    r = requests.get(url)
    return r.json()["price"]


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    price = get_price("BTCUSDT")

    if request.method == "POST":

        symbol = request.form.get("symbol")
        side = request.form.get("side")
        order_type = request.form.get("order_type")
        quantity = request.form.get("quantity")
        price_input = request.form.get("price")
        stop_price = request.form.get("stop_price")

        try:

            if order_type == "MARKET":
                result = place_market_order(symbol, side, quantity)

            elif order_type == "LIMIT":
                result = place_limit_order(symbol, side, quantity, price_input)

            elif order_type == "STOP":
                result = place_stop_order(symbol, side, quantity, price_input, stop_price)

        except Exception as e:
            result = str(e)

    return render_template("index.html", result=result, price=price)


if __name__ == "__main__":
    app.run(debug=True)