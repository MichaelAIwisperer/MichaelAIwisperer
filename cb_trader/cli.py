import argparse

from .config import load_config
from .client import make_client
from .services.market import list_top_products
from .services.accounts import list_accounts
from .runner import run_strategy
from .strategy.sma import SmaCrossoverStrategy


def cmd_public(args: argparse.Namespace) -> None:
    cfg = load_config()
    client = make_client(cfg)
    products = list_top_products(client, limit=args.limit)
    for pid in products:
        print(pid)


def cmd_accounts(args: argparse.Namespace) -> None:
    cfg = load_config()
    client = make_client(cfg)
    resp = list_accounts(client, limit=args.limit)
    for a in resp.accounts:
        print(f"{a.uuid} {a.currency} {a.available_balance.value} {a.available_balance.currency}")


def cmd_run(args: argparse.Namespace) -> None:
    cfg = load_config()
    client = make_client(cfg)
    strategy = SmaCrossoverStrategy(short_window=args.short, long_window=args.long)
    run_strategy(client, strategy, product_id=args.product, interval_seconds=args.interval, max_ticks=args.ticks)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cb", description="Coinbase trading scaffold")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("public", help="List public products")
    sp.add_argument("--limit", type=int, default=5)
    sp.set_defaults(func=cmd_public)

    sa = sub.add_parser("accounts", help="List authenticated accounts")
    sa.add_argument("--limit", type=int, default=50)
    sa.set_defaults(func=cmd_accounts)

    sr = sub.add_parser("run", help="Run SMA crossover strategy (paper)")
    sr.add_argument("--product", default="BTC-USD")
    sr.add_argument("--short", type=int, default=5)
    sr.add_argument("--long", type=int, default=20)
    sr.add_argument("--interval", type=float, default=2.0)
    sr.add_argument("--ticks", type=int, default=30)
    sr.set_defaults(func=cmd_run)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

