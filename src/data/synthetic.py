from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterator, List, Tuple

import torch
from torch.utils.data import IterableDataset


@dataclass
class SyntheticConfig:
    vocab_size: int = 32000
    max_seq_len: int = 128
    min_seq_len: int = 16


class SyntheticSequenceDataset(IterableDataset):
    def __init__(self, cfg: SyntheticConfig, num_batches: int, batch_size: int):
        super().__init__()
        self.cfg = cfg
        self.num_batches = num_batches
        self.batch_size = batch_size

    def __iter__(self) -> Iterator[Tuple[torch.Tensor, torch.Tensor, torch.Tensor]]:
        # Y is next-token prediction; label -100 masks padding
        for _ in range(self.num_batches):
            seq_len = random.randint(self.cfg.min_seq_len, self.cfg.max_seq_len)
            inputs: List[List[int]] = []
            labels: List[List[int]] = []
            attn_masks: List[List[int]] = []
            for _b in range(self.batch_size):
                ids = [random.randint(0, self.cfg.vocab_size - 1) for _ in range(seq_len)]
                inputs.append(ids[:-1])
                labels.append(ids[1:])
                attn_masks.append([1] * (seq_len - 1))

            max_t = max(len(x) for x in inputs)
            pad_id = 0
            x_pad = [x + [pad_id] * (max_t - len(x)) for x in inputs]
            y_pad = [y + [-100] * (max_t - len(y)) for y in labels]
            m_pad = [m + [0] * (max_t - len(m)) for m in attn_masks]

            yield (
                torch.tensor(x_pad, dtype=torch.long),
                torch.tensor(m_pad, dtype=torch.long),
                torch.tensor(y_pad, dtype=torch.long),
            )
