import json
import time
from datetime import datetime, timezone

import ccxt


CONFIG_PATH = "config.json"


def create_exchange(name: str):
    exchange_cls = getattr(ccxt, name)
    return exchange_cls({"enableRateLimit": True})


def fetch_last_price(exchange, symbol: str):
    ticker = exchange.fetch_ticker(symbol)
    return ticker.get("last")


def load_config(path: str):
    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)

    required_keys = [
        "exchange_a",
        "exchange_b",
        "symbols",
        "check_interval_sec",
        "spread_alert_pct",
    ]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing key in config: {key}")
    return config


def scan_once(ex_a, ex_b, exchange_a_name: str, exchange_b_name: str, symbols, spread_alert_pct: float):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"\n[{now}] scan")

    for symbol in symbols:
        try:
            price_a = fetch_last_price(ex_a, symbol)
            price_b = fetch_last_price(ex_b, symbol)
            if not price_a or not price_b:
                print(f"{symbol}: no price data")
                continue

            avg = (price_a + price_b) / 2
            spread_pct = abs(price_a - price_b) / avg * 100

            line = (
                f"{symbol}: {exchange_a_name}={price_a:.4f}, "
                f"{exchange_b_name}={price_b:.4f}, spread={spread_pct:.3f}%"
            )

            if spread_pct >= spread_alert_pct:
                line += "  <-- ALERT"
            print(line)
        except Exception as err:
            print(f"{symbol}: error: {err}")


def main():
    config = load_config(CONFIG_PATH)
    exchange_a_name = config["exchange_a"]
    exchange_b_name = config["exchange_b"]
    symbols = config["symbols"]
    check_interval_sec = config["check_interval_sec"]
    spread_alert_pct = config["spread_alert_pct"]

    print("Simple crypto spread scanner (read-only)")
    print(f"Exchanges: {exchange_a_name} vs {exchange_b_name}")
    print(f"Symbols: {', '.join(symbols)}")
    print(f"Alert threshold: {spread_alert_pct}%")
    print("Press Ctrl+C to stop.\n")

    ex_a = create_exchange(exchange_a_name)
    ex_b = create_exchange(exchange_b_name)

    while True:
        scan_once(ex_a, ex_b, exchange_a_name, exchange_b_name, symbols, spread_alert_pct)
        time.sleep(check_interval_sec)


if __name__ == "__main__":
    main()
