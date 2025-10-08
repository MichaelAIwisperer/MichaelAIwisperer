"""Portfolios API endpoints."""

from typing import TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from .rest_base import RESTBase


def create_portfolio(
    self: "RESTBase",
    name: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Create a new portfolio.
    
    Args:
        name: Name of the portfolio
        **kwargs: Additional parameters
        
    Returns:
        Dict containing created portfolio information
    """
    data = {"name": name, **kwargs}
    return self.post("/api/v3/brokerage/portfolios", data=data)


def get_portfolios(
    self: "RESTBase",
    portfolio_type: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get list of portfolios.
    
    Args:
        portfolio_type: Type of portfolio to filter by
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing list of portfolios
    """
    params = {**kwargs}
    if portfolio_type:
        params["portfolio_type"] = portfolio_type
        
    return self.get("/api/v3/brokerage/portfolios", params=params)


def edit_portfolio(
    self: "RESTBase",
    portfolio_uuid: str,
    name: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Edit a portfolio.
    
    Args:
        portfolio_uuid: The portfolio UUID
        name: New name for the portfolio
        **kwargs: Additional parameters
        
    Returns:
        Dict containing updated portfolio information
    """
    data = {"name": name, **kwargs}
    return self.put(f"/api/v3/brokerage/portfolios/{portfolio_uuid}", data=data)


def delete_portfolio(
    self: "RESTBase",
    portfolio_uuid: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Delete a portfolio.
    
    Args:
        portfolio_uuid: The portfolio UUID
        **kwargs: Additional parameters
        
    Returns:
        Dict containing deletion confirmation
    """
    return self.delete(f"/api/v3/brokerage/portfolios/{portfolio_uuid}", params=kwargs)


def get_portfolio_breakdown(
    self: "RESTBase",
    portfolio_uuid: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get portfolio breakdown.
    
    Args:
        portfolio_uuid: The portfolio UUID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing portfolio breakdown
    """
    return self.get(f"/api/v3/brokerage/portfolios/{portfolio_uuid}/breakdown", params=kwargs)


def move_portfolio_funds(
    self: "RESTBase",
    funds: Dict[str, Any],
    **kwargs
) -> Dict[str, Any]:
    """
    Move funds between portfolios.
    
    Args:
        funds: Dictionary containing fund movement details
        **kwargs: Additional parameters
        
    Returns:
        Dict containing fund movement confirmation
    """
    data = {"funds": funds, **kwargs}
    return self.post("/api/v3/brokerage/portfolios/move_funds", data=data)
