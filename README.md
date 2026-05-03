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

## Configuration

Edit `config.json`:

```json
{
  "exchange_a": "binance",
  "exchange_b": "bybit",
  "symbols": ["BTC/USDT", "ETH/USDT"],
  "check_interval_sec": 20,
  "spread_alert_pct": 0.3
}
```

- `exchange_a`, `exchange_b`: exchange IDs from `ccxt`
- `symbols`: list of pairs to monitor
- `check_interval_sec`: scan interval in seconds
- `spread_alert_pct`: alert threshold in percent

## What it does

- Pulls public prices from exchanges in `config.json`
- Checks symbols from `config.json`
- Prints an alert if spread is above configured threshold

No orders are sent. This is monitoring only.
