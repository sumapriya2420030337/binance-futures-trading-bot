# Binance Futures Testnet Trading Bot

A modular **Python trading bot** for placing orders on the **Binance USDT-M Futures Testnet**.

This project includes both:

• A **Command Line Interface (CLI)**  
• A **Lightweight Web UI**

The bot supports **Market, Limit, and Stop orders**, with **logging, validation, and error handling**.

This project demonstrates:

- Binance Futures API interaction
- Structured Python project design
- CLI development using argparse
- Web UI using Flask
- Logging and debugging
- Input validation and error handling

---

# Features

## Core Features

- Place **MARKET orders**
- Place **LIMIT orders**
- Place **STOP orders**
- Supports **BUY and SELL**
- CLI interface for placing trades
- Logging of API requests and responses
- Exception handling for API errors
- Input validation

---

## Bonus Features

- Lightweight **Web UI for placing trades**
- **Live BTC price display**
- Modular project architecture
- Request and response logging
- Error messages displayed in UI

---

# Project Structure
binance-futures-trading-bot
│
├── bot
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ └── logging_config.py
│
├── templates
│ └── index.html
│
├── static
│ └── styles.css
│
├── cli.py
├── ui.py
├── requirements.txt
├── README.md
└── .env

---

# Setup Instructions

## 1 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/binance-futures-trading-bot.git
cd binance-futures-trading-bot
## Setup Instructions

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac / Linux**

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Keys

Create a `.env` file in the root directory.

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

Generate API keys from:

https://testnet.binancefuture.com

---

# Running the Bot

## CLI Mode

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Example Output:

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

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

---

### Stop Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.01 --price 68000 --stop-price 67500
```

---

# Web Interface

Run the web UI:

```bash
python ui.py
```

Open browser:

```
http://127.0.0.1:5000
```

The UI allows you to:

- Enter symbol  
- Select order side  
- Select order type  
- Enter quantity  
- Enter limit price  
- Enter stop price  
- Place orders directly from the browser  

It also displays:

- Live BTC price  
- Order response messages  

---

# Logging

All API requests, responses, and errors are logged to:

```
logs/trading_bot.log
```

Example log entry:

```
INFO - {'orderId': 12550417640, 'symbol': 'BTCUSDT', 'status': 'NEW'}
```

---

# Error Handling

The application handles:

- Invalid CLI inputs  
- Missing parameters  
- Binance API errors  
- Network failures  

Errors returned from Binance are clearly displayed in:

- CLI output  
- Web UI response box  
- Log file  

---

# Assumptions

- The bot connects to **Binance Futures Testnet**
- A valid **testnet API key and secret** are required
- Orders must satisfy **Binance minimum trading limits**

---

# Dependencies

Dependencies listed in `requirements.txt`:

- requests  
- python-dotenv  
- flask  

Install using:

```bash
pip install -r requirements.txt
```

---

# Author

**Suma Priya Chittari**

---

# Project Summary

This project demonstrates:

- Python API integration  
- Modular code architecture  
- CLI development  
- Web UI integration  
- Logging and validation  

It acts as a **mini trading system prototype interacting with the Binance Futures Testnet**.
