# Binance Futures Testnet Trading Bot

A modular Python trading bot for placing orders on the **Binance USDT-M Futures Testnet**, featuring both a CLI and a lightweight Web UI.

---

## Features

| Feature | Details |
|---|---|
| Order Types | Market, Limit, Stop |
| Order Sides | BUY / SELL |
| Interfaces | CLI (`argparse`) + Web UI (`Flask`) |
| Extras | Live BTC price, request/response logging, input validation |

---

## Project Structure

```
binance-futures-trading-bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── styles.css
│
├── cli.py
├── ui.py
├── requirements.txt
├── README.md
└── .env
```

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
```

**Mac / Linux**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

> Get your testnet API keys at [testnet.binancefuture.com](https://testnet.binancefuture.com)

---

## Usage

### CLI Mode

**Market Order**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Limit Order**
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

**Stop Order**
```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.01 --price 68000 --stop-price 67500
```

**Example Output**
```
Order Request Summary
---------------------
Symbol:   BTCUSDT
Side:     BUY
Type:     MARKET
Quantity: 0.01

Order Response
--------------
Order ID:     12345678
Status:       NEW
Executed Qty: 0.000

SUCCESS: Order placed!
```

---

### Web UI Mode

```bash
python ui.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

The UI lets you fill in symbol, side, order type, quantity, and price fields, and displays live BTC price and order responses.

---

## Logging

All requests, responses, and errors are written to:

```
logs/trading_bot.log
```

Example entry:
```
INFO - {'orderId': 12550417640, 'symbol': 'BTCUSDT', 'status': 'NEW'}
```

---

## Error Handling

The bot handles and surfaces errors across all interfaces:

- Invalid or missing CLI arguments
- Binance API error responses
- Network failures

Errors appear in the CLI output, Web UI response box, and log file.

---

## Dependencies

```
requests
python-dotenv
flask
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Notes

- Connects to **Binance Futures Testnet only** — no real funds are used.
- Orders must meet Binance minimum trading size requirements.
- A valid testnet API key and secret are required.

---

## Author

**Suma Priya Chittari**
