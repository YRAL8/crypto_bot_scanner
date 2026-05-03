# Project Status and Next Steps

## Current Status

- Project folder: `~/my_code/crypto_bot`
- Git repo initialized
- First commit created and pushed
- Basic scanner works in read-only mode (no trading)

## Files in Project

- `spread_scanner.py` - compares prices on 2 exchanges and prints spread alerts
- `config.json` - scanner settings (exchanges, symbols, interval, threshold)
- `requirements.txt` - python dependency list
- `README.md` - setup and run instructions
- `.gitignore` - ignores `.venv` and python cache

## How To Run

```bash
cd ~/my_code/crypto_bot
source .venv/bin/activate
python3 spread_scanner.py
```

If `.venv` does not exist yet:

```bash
cd ~/my_code/crypto_bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 spread_scanner.py
```

## Next Tasks (Suggested Order)

1. Add CSV logging for each scan result
2. Include rough fee model to estimate net spread
3. Add paper-trade simulator (no real orders)
4. Add risk rules before any live-trading code

## Quick Prompt To Resume Later

Use this in a new chat:

`Open ~/my_code/crypto_bot and continue from NEXT_STEPS.md. Implement step 1 (config.json).`
