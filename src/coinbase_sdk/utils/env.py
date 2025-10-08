import os
from typing import Optional

from dotenv import load_dotenv

def load_env_if_present(path: Optional[str] = None) -> None:
    env_root = path or os.getcwd()
    aenv_path = os.path.join(env_root, "a.env")
    dotenv_path = os.path.join(env_root, ".env")

    if os.path.exists(aenv_path):
        load_dotenv(aenv_path, override=False)
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path, override=False)
