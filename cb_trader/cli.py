import argparse

from .config import load_config
from .client import make_client
from .services.market import list_top_products
from .services import market as market_svc
from .services.accounts import list_accounts
from .services.key_perms import get_permissions
from .services.fees import get_transaction_summary as fees_summary
from .services import orders as order_svc
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

    smc = sub.add_parser("candles", help="Get public candles")
    smc.add_argument("product")
    smc.add_argument("start")
    smc.add_argument("end")
    smc.add_argument("granularity")
    smc.add_argument("--limit", type=int)
    def _cand(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        resp = market_svc.get_candles(
            client,
            product_id=args.product,
            start=args.start,
            end=args.end,
            granularity=args.granularity,
            limit=args.limit,
        )
        print(resp.__dict__)
    smc.set_defaults(func=_cand)

    smt = sub.add_parser("trades", help="Get public market trades snapshot")
    smt.add_argument("product")
    smt.add_argument("limit", type=int)
    smt.add_argument("--start")
    smt.add_argument("--end")
    def _trd(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        resp = market_svc.get_market_trades(
            client,
            product_id=args.product,
            limit=args.limit,
            start=args.start,
            end=args.end,
        )
        print(resp.__dict__)
    smt.set_defaults(func=_trd)

    so = sub.add_parser("order", help="Order actions")
    so_sub = so.add_subparsers(dest="subcmd", required=True)

    som_b = so_sub.add_parser("market-buy", help="Market buy (paper by default)")
    som_b.add_argument("product")
    som_b.add_argument("--quote_size")
    som_b.add_argument("--base_size")
    som_b.add_argument("--live", action="store_true", help="Execute live order")
    def _omb(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        if args.live:
            resp = order_svc.market_buy(client, product_id=args.product, quote_size=args.quote_size)
        else:
            resp = order_svc.preview_market_buy(
                client, product_id=args.product, quote_size=args.quote_size, base_size=args.base_size
            )
        print(resp.__dict__)
    som_b.set_defaults(func=_omb)

    som_s = so_sub.add_parser("market-sell", help="Market sell (paper by default)")
    som_s.add_argument("product")
    som_s.add_argument("--base_size", required=True)
    som_s.add_argument("--live", action="store_true", help="Execute live order")
    def _oms(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        if args.live:
            resp = order_svc.market_sell(client, product_id=args.product, base_size=args.base_size)
        else:
            resp = order_svc.preview_market_sell(client, product_id=args.product, base_size=args.base_size)
        print(resp.__dict__)
    som_s.set_defaults(func=_oms)

    sf = sub.add_parser("fees", help="Show transaction summary (fees)")
    sf.add_argument("--product_type")
    sf.add_argument("--contract_expiry_type")
    sf.add_argument("--product_venue")
    def _f(args: argparse.Namespace) -> None:
        cfg = load_config()
        client = make_client(cfg)
        resp = fees_summary(
            client,
            product_type=args.product_type,
            contract_expiry_type=args.contract_expiry_type,
            product_venue=args.product_venue,
        )
        print(resp.__dict__)
    sf.set_defaults(func=_f)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

