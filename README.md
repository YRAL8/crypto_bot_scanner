# Crypto Bot Starter

Simple read-only scanner that compares prices between two exchanges and prints spread alerts.

## Setup

```bash
cd ~/my_code/crypto_bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 spread_scanner.py
```

## What it does

- Pulls public prices from `binance` and `bybit`
- Checks `BTC/USDT` and `ETH/USDT`
- Prints an alert if spread is above `0.30%`

No orders are sent. This is monitoring only.
