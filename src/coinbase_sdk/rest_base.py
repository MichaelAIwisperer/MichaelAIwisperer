from __future__ import annotations

import json
import logging
from typing import Any, Dict, Mapping, Optional

import requests

from .config import SDKConfig, load_config_from_env

class RESTBase:
    def __init__(
        self,
        config: Optional[SDKConfig] = None,
        *,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout_seconds: Optional[int] = None,
        verbose_logging: Optional[bool] = None,
        rate_limit_headers: Optional[bool] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.config = config or load_config_from_env()

        if api_key is not None:
            self.config.api_key = api_key
        if api_secret is not None:
            self.config.api_secret = api_secret
        if base_url is not None:
            self.config.base_url = base_url
        if timeout_seconds is not None:
            self.config.timeout_seconds = timeout_seconds
        if verbose_logging is not None:
            self.config.verbose_logging = verbose_logging
        if rate_limit_headers is not None:
            self.config.rate_limit_headers = rate_limit_headers

        self.session = session or requests.Session()
        self._logger = logging.getLogger("coinbase_sdk")
        if self.config.verbose_logging:
            logging.basicConfig(level=logging.DEBUG)

        self._default_headers: Dict[str, str] = {
            "User-Agent": "coinbase-sdk/0.0.1",
            "Accept": "application/json",
        }
        if self.config.api_key:
            self._default_headers["Authorization"] = f"Bearer {self.config.api_key}"

    @property
    def base_url(self) -> str:
        return self.config.base_url.rstrip("/")

    def _build_url(self, path: str) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return f"{self.base_url}/{path.lstrip(/)}"

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        json_body: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout_seconds: Optional[int] = None,
    ) -> Dict[str, Any]:
        url = self._build_url(path)
        merged_headers: Dict[str, str] = dict(self._default_headers)
        if headers:
            merged_headers.update(headers)

        timeout = timeout_seconds or self.config.timeout_seconds

        if self.config.verbose_logging:
            self._logger.debug(
                "HTTP %s %s params=%s json=%s headers=%s",
                method,
                url,
                dict(params or {}),
                json.dumps(json_body or {}),
                {k: ("***" if k.lower().startswith("authorization") else v) for k, v in merged_headers.items()},
            )

        response = self.session.request(
            method=method.upper(),
            url=url,
            params=dict(params or {}),
            json=json_body,
            headers=merged_headers,
            timeout=timeout,
        )
        if self.config.verbose_logging:
            self._logger.debug("HTTP %s -> %s", method.upper(), response.status_code)
        response.raise_for_status()
        if response.content and response.headers.get("Content-Type", "").startswith("application/json"):
            return response.json()
        return {"status_code": response.status_code, "content": response.text}
