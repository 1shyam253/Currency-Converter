#!/usr/bin/env python3
"""Currency Converter - convert between currencies using fixed offline rates (no API key)."""
import argparse
# Rates relative to 1 USD, for illustration. Update them when you need current rates.
RATES = {"USD": 1.0, "EUR": 0.92, "GBP": 0.79, "INR": 83.5, "JPY": 149.0, "AUD": 1.52, "CAD": 1.36}

def convert(amount, source, target):
    return amount / RATES[source] * RATES[target]

def main():
    p = argparse.ArgumentParser(description="Currency Converter (offline, fixed rates)")
    p.add_argument("amount", type=float, help="Amount to convert")
    p.add_argument("--from", dest="source", default="USD", choices=RATES, help="Source currency")
    p.add_argument("--to", dest="target", default="INR", choices=RATES, help="Target currency")
    args = p.parse_args()
    result = convert(args.amount, args.source, args.target)
    print(f"{args.amount:.2f} {args.source} = {result:.2f} {args.target}")

if __name__ == "__main__":
    main()
