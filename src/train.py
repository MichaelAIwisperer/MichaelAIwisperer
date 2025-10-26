from __future__ import annotations

import argparse
from dataclasses import asdict
from pathlib import Path

import torch
from torch.optim import AdamW
from torch.utils.data import DataLoader
from tqdm import tqdm

from models.transformer import TransformerConfig, TransformerModel
from data.synthetic import SyntheticConfig, SyntheticSequenceDataset


def get_device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def train(args: argparse.Namespace) -> None:
    device = get_device()

    cfg = TransformerConfig(
        vocab_size=args.vocab_size,
        max_seq_len=args.max_seq_len,
        d_model=args.d_model,
        n_heads=args.n_heads,
        d_ff=args.d_ff,
        n_layers=args.n_layers,
        dropout=args.dropout,
    )

    model = TransformerModel(cfg).to(device)
    optim = AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)

    data_cfg = SyntheticConfig(
        vocab_size=args.vocab_size,
        max_seq_len=args.max_seq_len,
        min_seq_len=max(8, args.max_seq_len // 4),
    )
    dataset = SyntheticSequenceDataset(data_cfg, num_batches=args.steps, batch_size=args.batch_size)
    loader = DataLoader(dataset, batch_size=None)

    model.train()
    progress = tqdm(loader, total=args.steps, ncols=100)
    for step, batch in enumerate(progress, start=1):
        input_ids, attention_mask, labels = [x.to(device) for x in batch]
        _, loss = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)

        optim.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optim.step()

        progress.set_description(f"loss={loss.item():.4f}")

        if step % args.ckpt_every == 0:
            save_dir = Path(args.out_dir)
            save_dir.mkdir(parents=True, exist_ok=True)
            ckpt_path = save_dir / f"step_{step}.pt"
            torch.save({
                "model": model.state_dict(),
                "config": asdict(cfg),
                "step": step,
            }, ckpt_path)

    # final save
    save_dir = Path(args.out_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    torch.save({
        "model": model.state_dict(),
        "config": asdict(cfg),
        "step": step,
    }, save_dir / "final.pt")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--vocab_size", type=int, default=8192)
    p.add_argument("--max_seq_len", type=int, default=128)
    p.add_argument("--d_model", type=int, default=256)
    p.add_argument("--n_heads", type=int, default=8)
    p.add_argument("--d_ff", type=int, default=1024)
    p.add_argument("--n_layers", type=int, default=4)
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--steps", type=int, default=50)
    p.add_argument("--lr", type=float, default=3e-4)
    p.add_argument("--ckpt_every", type=int, default=25)
    p.add_argument("--out_dir", type=str, default="checkpoints")

    args = p.parse_args()
    train(args)
