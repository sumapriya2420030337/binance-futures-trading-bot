import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


def sign_params(params):

    query_string = "&".join([f"{k}={v}" for k, v in params.items()])

    signature = hmac.new(
        API_SECRET.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

    return query_string + "&signature=" + signature


def send_signed_request(method, endpoint, params):

    params["timestamp"] = int(time.time() * 1000)

    query = sign_params(params)

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    url = BASE_URL + endpoint + "?" + query

    if method == "POST":
        response = requests.post(url, headers=headers)

    elif method == "GET":
        response = requests.get(url, headers=headers)

    else:
        raise ValueError("Unsupported method")

    return response.json()