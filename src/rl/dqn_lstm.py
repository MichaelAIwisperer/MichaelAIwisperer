from dataclasses import dataclass
from typing import Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


class DQNLSTM(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, num_actions: int):
        super().__init__()
        self.feature = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
        )
        self.lstm = nn.LSTM(input_size=128, hidden_size=hidden_dim, batch_first=True)
        self.head = nn.Linear(hidden_dim, num_actions)

    def forward(self, x: torch.Tensor, h: Tuple[torch.Tensor, torch.Tensor] | None = None):
        # x: [batch, seq, input_dim]
        b, t, d = x.shape
        x = x.reshape(b * t, d)
        x = self.feature(x)
        x = x.view(b, t, -1)
        x, h = self.lstm(x, h)
        q = self.head(x)  # [batch, seq, num_actions]
        return q, h


@dataclass
class DQNConfig:
    learning_rate: float = 1e-4
    gamma: float = 0.99
    tau: float = 0.005


class DQNAgent:
    def __init__(self, state_dim: int, num_actions: int, hidden_dim: int, cfg: DQNConfig):
        self.policy_net = DQNLSTM(state_dim, hidden_dim, num_actions)
        self.target_net = DQNLSTM(state_dim, hidden_dim, num_actions)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=cfg.learning_rate)
        self.gamma = cfg.gamma
        self.tau = cfg.tau

    def select_action(self, state: np.ndarray, epsilon: float = 0.1) -> int:
        if np.random.rand() < epsilon:
            return np.random.randint(0, self.num_actions)
        with torch.no_grad():
            state_t = torch.tensor(state, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
            q, _ = self.policy_net(state_t)
            return int(torch.argmax(q[0, -1]).item())

    @property
    def num_actions(self) -> int:
        return self.policy_net.head.out_features

    def update(self, batch):
        # Placeholder for training step
        pass

    def soft_update_target(self):
        with torch.no_grad():
            for target_param, param in zip(self.target_net.parameters(), self.policy_net.parameters()):
                target_param.data.copy_(self.tau * param.data + (1.0 - self.tau) * target_param.data)
