"""Perpetuals API endpoints."""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from .rest_base import RESTBase


def allocate_portfolio(
    self: "RESTBase",
    portfolio_uuid: str,
    symbol: str,
    amount: str,
    currency: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Allocate portfolio funds to perpetuals.
    
    Args:
        portfolio_uuid: The portfolio UUID
        symbol: The symbol to allocate to
        amount: Amount to allocate
        currency: Currency of allocation
        **kwargs: Additional parameters
        
    Returns:
        Dict containing allocation information
    """
    data = {
        "portfolio_uuid": portfolio_uuid,
        "symbol": symbol,
        "amount": amount,
        "currency": currency,
        **kwargs
    }
    return self.post("/api/v3/brokerage/intx/allocate", data=data)


def get_perps_portfolio_summary(
    self: "RESTBase",
    portfolio_uuid: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get perpetuals portfolio summary.
    
    Args:
        portfolio_uuid: The portfolio UUID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing portfolio summary
    """
    return self.get(f"/api/v3/brokerage/intx/portfolio/{portfolio_uuid}", params=kwargs)


def list_perps_positions(
    self: "RESTBase",
    portfolio_uuid: str,
    **kwargs
) -> Dict[str, Any]:
    """
    List perpetuals positions.
    
    Args:
        portfolio_uuid: The portfolio UUID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing list of positions
    """
    return self.get(f"/api/v3/brokerage/intx/positions/{portfolio_uuid}", params=kwargs)


def get_perps_position(
    self: "RESTBase",
    portfolio_uuid: str,
    symbol: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get a specific perpetuals position.
    
    Args:
        portfolio_uuid: The portfolio UUID
        symbol: The symbol
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing position information
    """
    return self.get(f"/api/v3/brokerage/intx/positions/{portfolio_uuid}/{symbol}", params=kwargs)


def get_perps_portfolio_balances(
    self: "RESTBase",
    portfolio_uuid: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get perpetuals portfolio balances.
    
    Args:
        portfolio_uuid: The portfolio UUID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing portfolio balances
    """
    return self.get(f"/api/v3/brokerage/intx/balances/{portfolio_uuid}", params=kwargs)


def opt_in_or_out_multi_asset_collateral(
    self: "RESTBase",
    portfolio_uuid: str,
    multi_asset_collateral_enabled: bool,
    **kwargs
) -> Dict[str, Any]:
    """
    Opt in or out of multi-asset collateral.
    
    Args:
        portfolio_uuid: The portfolio UUID
        multi_asset_collateral_enabled: Whether to enable multi-asset collateral
        **kwargs: Additional parameters
        
    Returns:
        Dict containing updated settings
    """
    data = {
        "portfolio_uuid": portfolio_uuid,
        "multi_asset_collateral_enabled": multi_asset_collateral_enabled,
        **kwargs
    }
    return self.post("/api/v3/brokerage/intx/multi_asset_collateral", data=data)
