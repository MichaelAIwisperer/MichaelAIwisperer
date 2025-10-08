import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    api_key: Optional[str] = Field(default=None, alias="COINBASE_API_KEY")
    api_secret: Optional[str] = Field(default=None, alias="COINBASE_API_SECRET")
    api_key_file: Optional[str] = Field(default=None, alias="COINBASE_API_KEY_FILE")
    timeout_seconds: int = Field(default=30, alias="COINBASE_TIMEOUT")
    verbose: bool = Field(default=False, alias="COINBASE_VERBOSE")

    class Config:
        populate_by_name = True


def load_config() -> AppConfig:
    load_dotenv()
    return AppConfig(
        COINBASE_API_KEY=os.getenv("COINBASE_API_KEY"),
        COINBASE_API_SECRET=os.getenv("COINBASE_API_SECRET"),
        COINBASE_API_KEY_FILE=os.getenv("COINBASE_API_KEY_FILE"),
        COINBASE_TIMEOUT=int(os.getenv("COINBASE_TIMEOUT", "30")),
        COINBASE_VERBOSE=os.getenv("COINBASE_VERBOSE", "false").lower() == "true",
    )

