# Binance Futures Testnet Trading Bot

## Overview

This project is a Python command-line application that places **MARKET** and **LIMIT** orders on the **Binance USDT-M Futures Testnet**.

The application demonstrates:

* Interaction with the Binance Futures Testnet API
* A structured and modular Python codebase
* CLI-based user input using `argparse`
* Logging of requests, responses, and errors
* Basic input validation and exception handling

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Supports **BUY** and **SELL** order sides
* Command-line interface for order input
* API request and response logging
* Error handling for invalid input and API failures

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API request & authentication
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # CLI input validation
│   └── logging_config.py  # Logging configuration
│
├── logs/
│   └── trading_bot.log    # API request/response logs
│
├── cli.py                 # CLI entry point
├── requirements.txt       # Python dependencies
├── .env                   # API credentials (not committed)
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd trading_bot
```

---

### 2. Create a virtual environment

```
python -m venv .venv
```

Activate it:

Windows

```
.venv\Scripts\activate
```

Mac/Linux

```
source .venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure API keys

Create a `.env` file in the project root:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

API keys must be generated from:

```
https://testnet.binancefuture.com
```

---

## Running the Bot

### Place a MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Example output:

```
Order Request Summary
---------------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

Order Response
--------------
Order ID: 12345678
Status: NEW
Executed Qty: 0.000

SUCCESS: Order placed!
```

---

### Place a LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

---

## Logging

All API requests, responses, and errors are logged to:

```
logs/trading_bot.log
```

Example log entry:

```
INFO - {'orderId': 12550417640, 'symbol': 'BTCUSDT', 'status': 'NEW'}
```

---

## Error Handling

The application handles:

* Invalid CLI inputs
* Missing parameters
* Binance API errors
* Network failures

Errors returned from the Binance API are printed clearly in the CLI and logged to the log file.

---

## Assumptions

* The application uses **Binance USDT-M Futures Testnet**
* A valid testnet API key and secret are required
* Order quantity must satisfy Binance minimum trading limits

---

## Dependencies

Listed in `requirements.txt`:

```
requests
python-dotenv
```

---

## Author

Suma Priya Chittari
