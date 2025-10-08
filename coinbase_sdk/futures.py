"""Futures API endpoints."""

from typing import TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from .rest_base import RESTBase


def get_futures_balance_summary(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    Get futures balance summary.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing futures balance summary
    """
    return self.get("/api/v3/brokerage/cfm/balance_summary", params=kwargs)


def list_futures_positions(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    List all futures positions.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing list of futures positions
    """
    return self.get("/api/v3/brokerage/cfm/positions", params=kwargs)


def get_futures_position(
    self: "RESTBase",
    product_id: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get a specific futures position.
    
    Args:
        product_id: The product ID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing futures position information
    """
    return self.get(f"/api/v3/brokerage/cfm/positions/{product_id}", params=kwargs)


def schedule_futures_sweep(
    self: "RESTBase",
    usd_amount: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Schedule a futures sweep.
    
    Args:
        usd_amount: Amount in USD to sweep
        **kwargs: Additional parameters
        
    Returns:
        Dict containing sweep schedule information
    """
    data = {"usd_amount": usd_amount, **kwargs}
    return self.post("/api/v3/brokerage/cfm/sweeps/schedule", data=data)


def list_futures_sweeps(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    List all futures sweeps.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing list of futures sweeps
    """
    return self.get("/api/v3/brokerage/cfm/sweeps", params=kwargs)


def cancel_pending_futures_sweep(
    self: "RESTBase",
    sweep_id: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Cancel a pending futures sweep.
    
    Args:
        sweep_id: The sweep ID to cancel
        **kwargs: Additional parameters
        
    Returns:
        Dict containing cancellation confirmation
    """
    return self.delete(f"/api/v3/brokerage/cfm/sweeps/{sweep_id}", params=kwargs)


def get_intraday_margin_setting(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    Get intraday margin setting.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing intraday margin setting
    """
    return self.get("/api/v3/brokerage/cfm/intraday/margin_setting", params=kwargs)


def get_current_margin_window(
    self: "RESTBase",
    margin_profile_type: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get current margin window.
    
    Args:
        margin_profile_type: Type of margin profile
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing current margin window information
    """
    params = {"margin_profile_type": margin_profile_type, **kwargs}
    return self.get("/api/v3/brokerage/cfm/intraday/current_margin_window", params=params)


def set_intraday_margin_setting(
    self: "RESTBase",
    setting: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Set intraday margin setting.
    
    Args:
        setting: The margin setting to apply
        **kwargs: Additional parameters
        
    Returns:
        Dict containing updated margin setting
    """
    data = {"setting": setting, **kwargs}
    return self.post("/api/v3/brokerage/cfm/intraday/margin_setting", data=data)
