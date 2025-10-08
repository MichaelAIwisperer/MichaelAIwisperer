import argparse

from .config import load_config
from .client import make_client
from .services.market import list_top_products
from .services.accounts import list_accounts
from .services.key_perms import get_permissions
from .runner import run_strategy
from .services import convert as convert_svc
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

    sc = sub.add_parser("convert", help="Create/get/commit convert trades")
    sc_sub = sc.add_subparsers(dest="subcmd", required=True)

    sc_q = sc_sub.add_parser("quote", help="Create convert quote")
    sc_q.add_argument("from_account")
    sc_q.add_argument("to_account")
    sc_q.add_argument("amount")
    sc_q.add_argument("--user_incentive_id")
    sc_q.add_argument("--code_val")
    def _q(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        resp = convert_svc.create_quote(
            client,
            from_account=args.from_account,
            to_account=args.to_account,
            amount=args.amount,
            user_incentive_id=args.user_incentive_id,
            code_val=args.code_val,
        )
        print(resp.__dict__)
    sc_q.set_defaults(func=_q)

    sc_g = sc_sub.add_parser("get", help="Get convert trade")
    sc_g.add_argument("trade_id")
    sc_g.add_argument("from_account")
    sc_g.add_argument("to_account")
    def _g(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        resp = convert_svc.get_trade(
            client,
            trade_id=args.trade_id,
            from_account=args.from_account,
            to_account=args.to_account,
        )
        print(resp.__dict__)
    sc_g.set_defaults(func=_g)

    sc_c = sc_sub.add_parser("commit", help="Commit convert trade")
    sc_c.add_argument("trade_id")
    sc_c.add_argument("from_account")
    sc_c.add_argument("to_account")
    def _c(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        resp = convert_svc.commit_trade(
            client,
            trade_id=args.trade_id,
            from_account=args.from_account,
            to_account=args.to_account,
        )
        print(resp.__dict__)
    sc_c.set_defaults(func=_c)

    sk = sub.add_parser("key-perms", help="Show API key permissions (auth)")
    def _k(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        resp = get_permissions(client)
        print(resp.__dict__)
    sk.set_defaults(func=_k)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

