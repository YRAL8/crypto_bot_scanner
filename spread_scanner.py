import time
from datetime import datetime, timezone

import ccxt


EXCHANGE_A = "binance"
EXCHANGE_B = "bybit"
SYMBOLS = ["BTC/USDT", "ETH/USDT"]
CHECK_INTERVAL_SEC = 20
SPREAD_ALERT_PCT = 0.30


def create_exchange(name: str):
    exchange_cls = getattr(ccxt, name)
    return exchange_cls({"enableRateLimit": True})


def fetch_last_price(exchange, symbol: str):
    ticker = exchange.fetch_ticker(symbol)
    return ticker.get("last")


def scan_once(ex_a, ex_b):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"\n[{now}] scan")

    for symbol in SYMBOLS:
        try:
            price_a = fetch_last_price(ex_a, symbol)
            price_b = fetch_last_price(ex_b, symbol)
            if not price_a or not price_b:
                print(f"{symbol}: no price data")
                continue

            avg = (price_a + price_b) / 2
            spread_pct = abs(price_a - price_b) / avg * 100

            line = (
                f"{symbol}: {EXCHANGE_A}={price_a:.4f}, "
                f"{EXCHANGE_B}={price_b:.4f}, spread={spread_pct:.3f}%"
            )

            if spread_pct >= SPREAD_ALERT_PCT:
                line += "  <-- ALERT"
            print(line)
        except Exception as err:
            print(f"{symbol}: error: {err}")


def main():
    print("Simple crypto spread scanner (read-only)")
    print(f"Exchanges: {EXCHANGE_A} vs {EXCHANGE_B}")
    print(f"Symbols: {', '.join(SYMBOLS)}")
    print(f"Alert threshold: {SPREAD_ALERT_PCT}%")
    print("Press Ctrl+C to stop.\n")

    ex_a = create_exchange(EXCHANGE_A)
    ex_b = create_exchange(EXCHANGE_B)

    while True:
        scan_once(ex_a, ex_b)
        time.sleep(CHECK_INTERVAL_SEC)


if __name__ == "__main__":
    main()
