"""Orders API endpoints."""

from typing import TYPE_CHECKING, Dict, Any, Optional, List

if TYPE_CHECKING:
    from .rest_base import RESTBase


def create_order(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    order_configuration: Dict[str, Any],
    **kwargs
) -> Dict[str, Any]:
    """
    Create an order.
    
    Args:
        client_order_id: Client-specified order ID
        product_id: The product ID
        side: 'BUY' or 'SELL'
        order_configuration: Order configuration object
        **kwargs: Additional parameters
        
    Returns:
        Dict containing order information
    """
    data = {
        "client_order_id": client_order_id,
        "product_id": product_id,
        "side": side,
        "order_configuration": order_configuration,
        **kwargs
    }
    return self.post("/api/v3/brokerage/orders", data=data)


def cancel_orders(
    self: "RESTBase",
    order_ids: List[str],
    **kwargs
) -> Dict[str, Any]:
    """
    Cancel one or more orders.
    
    Args:
        order_ids: List of order IDs to cancel
        **kwargs: Additional parameters
        
    Returns:
        Dict containing cancellation results
    """
    data = {"order_ids": order_ids, **kwargs}
    return self.post("/api/v3/brokerage/orders/batch_cancel", data=data)


def edit_order(
    self: "RESTBase",
    order_id: str,
    price: Optional[str] = None,
    size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Edit an order.
    
    Args:
        order_id: The order ID to edit
        price: New price
        size: New size
        **kwargs: Additional parameters
        
    Returns:
        Dict containing updated order information
    """
    data = {**kwargs}
    if price:
        data["price"] = price
    if size:
        data["size"] = size
        
    return self.post(f"/api/v3/brokerage/orders/edit/{order_id}", data=data)


def list_orders(
    self: "RESTBase",
    product_id: Optional[str] = None,
    order_status: Optional[List[str]] = None,
    limit: Optional[int] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    List orders.
    
    Args:
        product_id: Filter by product ID
        order_status: Filter by order status
        limit: Number of orders to return
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing list of orders
    """
    params = {**kwargs}
    if product_id:
        params["product_id"] = product_id
    if order_status:
        params["order_status"] = order_status
    if limit is not None:
        params["limit"] = limit
        
    return self.get("/api/v3/brokerage/orders/batch", params=params)


def get_fills(
    self: "RESTBase",
    order_id: Optional[str] = None,
    product_id: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get fills for orders.
    
    Args:
        order_id: Filter by order ID
        product_id: Filter by product ID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing fills information
    """
    params = {**kwargs}
    if order_id:
        params["order_id"] = order_id
    if product_id:
        params["product_id"] = product_id
        
    return self.get("/api/v3/brokerage/orders/historical/fills", params=params)


def get_order(self: "RESTBase", order_id: str, **kwargs) -> Dict[str, Any]:
    """
    Get a specific order.
    
    Args:
        order_id: The order ID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing order information
    """
    return self.get(f"/api/v3/brokerage/orders/historical/{order_id}", params=kwargs)


def preview_order(
    self: "RESTBase",
    product_id: str,
    side: str,
    order_configuration: Dict[str, Any],
    **kwargs
) -> Dict[str, Any]:
    """
    Preview an order.
    
    Args:
        product_id: The product ID
        side: 'BUY' or 'SELL'
        order_configuration: Order configuration object
        **kwargs: Additional parameters
        
    Returns:
        Dict containing order preview
    """
    data = {
        "product_id": product_id,
        "side": side,
        "order_configuration": order_configuration,
        **kwargs
    }
    return self.post("/api/v3/brokerage/orders/preview", data=data)


def preview_edit_order(
    self: "RESTBase",
    order_id: str,
    price: Optional[str] = None,
    size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Preview an order edit.
    
    Args:
        order_id: The order ID to edit
        price: New price
        size: New size
        **kwargs: Additional parameters
        
    Returns:
        Dict containing edit preview
    """
    data = {**kwargs}
    if price:
        data["price"] = price
    if size:
        data["size"] = size
        
    return self.post(f"/api/v3/brokerage/orders/edit_preview/{order_id}", data=data)


def close_position(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Close a position.
    
    Args:
        client_order_id: Client-specified order ID
        product_id: The product ID
        **kwargs: Additional parameters
        
    Returns:
        Dict containing position closure information
    """
    data = {
        "client_order_id": client_order_id,
        "product_id": product_id,
        **kwargs
    }
    return self.post("/api/v3/brokerage/orders/close_position", data=data)


# Market Order Helper Functions
def market_order(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """Create a market order."""
    order_config = {"market_market_ioc": {}}
    if quote_size:
        order_config["market_market_ioc"]["quote_size"] = quote_size
    if base_size:
        order_config["market_market_ioc"]["base_size"] = base_size
        
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def market_order_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """Create a market buy order."""
    return market_order(self, client_order_id, product_id, "BUY", quote_size, base_size, **kwargs)


def market_order_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """Create a market sell order."""
    return market_order(self, client_order_id, product_id, "SELL", quote_size, base_size, **kwargs)


# Limit Order GTC (Good Till Canceled) Functions
def limit_order_gtc(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit order (Good Till Canceled)."""
    order_config = {
        "limit_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "post_only": post_only
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def limit_order_gtc_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit buy order (Good Till Canceled)."""
    return limit_order_gtc(self, client_order_id, product_id, "BUY", base_size, limit_price, post_only, **kwargs)


def limit_order_gtc_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit sell order (Good Till Canceled)."""
    return limit_order_gtc(self, client_order_id, product_id, "SELL", base_size, limit_price, post_only, **kwargs)


# Limit Order GTD (Good Till Date) Functions
def limit_order_gtd(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit order (Good Till Date)."""
    order_config = {
        "limit_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "end_time": end_time,
            "post_only": post_only
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def limit_order_gtd_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit buy order (Good Till Date)."""
    return limit_order_gtd(self, client_order_id, product_id, "BUY", base_size, limit_price, end_time, post_only, **kwargs)


def limit_order_gtd_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit sell order (Good Till Date)."""
    return limit_order_gtd(self, client_order_id, product_id, "SELL", base_size, limit_price, end_time, post_only, **kwargs)


# Limit Order IOC (Immediate Or Cancel) Functions
def limit_order_ioc(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit order (Immediate Or Cancel)."""
    order_config = {
        "limit_limit_ioc": {
            "base_size": base_size,
            "limit_price": limit_price
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def limit_order_ioc_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit buy order (Immediate Or Cancel)."""
    return limit_order_ioc(self, client_order_id, product_id, "BUY", base_size, limit_price, **kwargs)


def limit_order_ioc_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit sell order (Immediate Or Cancel)."""
    return limit_order_ioc(self, client_order_id, product_id, "SELL", base_size, limit_price, **kwargs)


# Limit Order FOK (Fill Or Kill) Functions
def limit_order_fok(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit order (Fill Or Kill)."""
    order_config = {
        "limit_limit_fok": {
            "base_size": base_size,
            "limit_price": limit_price
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def limit_order_fok_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit buy order (Fill Or Kill)."""
    return limit_order_fok(self, client_order_id, product_id, "BUY", base_size, limit_price, **kwargs)


def limit_order_fok_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a limit sell order (Fill Or Kill)."""
    return limit_order_fok(self, client_order_id, product_id, "SELL", base_size, limit_price, **kwargs)


# Stop Limit Order GTC Functions
def stop_limit_order_gtc(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a stop limit order (Good Till Canceled)."""
    order_config = {
        "stop_limit_stop_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "stop_direction": stop_direction
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def stop_limit_order_gtc_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a stop limit buy order (Good Till Canceled)."""
    return stop_limit_order_gtc(self, client_order_id, product_id, "BUY", base_size, limit_price, stop_price, "STOP_DIRECTION_STOP_UP", **kwargs)


def stop_limit_order_gtc_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a stop limit sell order (Good Till Canceled)."""
    return stop_limit_order_gtc(self, client_order_id, product_id, "SELL", base_size, limit_price, stop_price, "STOP_DIRECTION_STOP_DOWN", **kwargs)


# Stop Limit Order GTD Functions
def stop_limit_order_gtd(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a stop limit order (Good Till Date)."""
    order_config = {
        "stop_limit_stop_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "end_time": end_time,
            "stop_direction": stop_direction
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def stop_limit_order_gtd_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a stop limit buy order (Good Till Date)."""
    return stop_limit_order_gtd(self, client_order_id, product_id, "BUY", base_size, limit_price, stop_price, end_time, "STOP_DIRECTION_STOP_UP", **kwargs)


def stop_limit_order_gtd_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a stop limit sell order (Good Till Date)."""
    return stop_limit_order_gtd(self, client_order_id, product_id, "SELL", base_size, limit_price, stop_price, end_time, "STOP_DIRECTION_STOP_DOWN", **kwargs)


# Trigger Bracket Order GTC Functions
def trigger_bracket_order_gtc(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a trigger bracket order (Good Till Canceled)."""
    order_config = {
        "trigger_bracket_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def trigger_bracket_order_gtc_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a trigger bracket buy order (Good Till Canceled)."""
    return trigger_bracket_order_gtc(self, client_order_id, product_id, "BUY", base_size, limit_price, stop_trigger_price, **kwargs)


def trigger_bracket_order_gtc_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a trigger bracket sell order (Good Till Canceled)."""
    return trigger_bracket_order_gtc(self, client_order_id, product_id, "SELL", base_size, limit_price, stop_trigger_price, **kwargs)


# Trigger Bracket Order GTD Functions
def trigger_bracket_order_gtd(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a trigger bracket order (Good Till Date)."""
    order_config = {
        "trigger_bracket_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price,
            "end_time": end_time
        }
    }
    return create_order(self, client_order_id, product_id, side, order_config, **kwargs)


def trigger_bracket_order_gtd_buy(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a trigger bracket buy order (Good Till Date)."""
    return trigger_bracket_order_gtd(self, client_order_id, product_id, "BUY", base_size, limit_price, stop_trigger_price, end_time, **kwargs)


def trigger_bracket_order_gtd_sell(
    self: "RESTBase",
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Create a trigger bracket sell order (Good Till Date)."""
    return trigger_bracket_order_gtd(self, client_order_id, product_id, "SELL", base_size, limit_price, stop_trigger_price, end_time, **kwargs)


# Preview Functions for Market Orders
def preview_market_order(
    self: "RESTBase",
    product_id: str,
    side: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """Preview a market order."""
    order_config = {"market_market_ioc": {}}
    if quote_size:
        order_config["market_market_ioc"]["quote_size"] = quote_size
    if base_size:
        order_config["market_market_ioc"]["base_size"] = base_size
        
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_market_order_buy(
    self: "RESTBase",
    product_id: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """Preview a market buy order."""
    return preview_market_order(self, product_id, "BUY", quote_size, base_size, **kwargs)


def preview_market_order_sell(
    self: "RESTBase",
    product_id: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """Preview a market sell order."""
    return preview_market_order(self, product_id, "SELL", quote_size, base_size, **kwargs)


# Preview Functions for Limit Orders GTC
def preview_limit_order_gtc(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit order (Good Till Canceled)."""
    order_config = {
        "limit_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "post_only": post_only
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_limit_order_gtc_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit buy order (Good Till Canceled)."""
    return preview_limit_order_gtc(self, product_id, "BUY", base_size, limit_price, post_only, **kwargs)


def preview_limit_order_gtc_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit sell order (Good Till Canceled)."""
    return preview_limit_order_gtc(self, product_id, "SELL", base_size, limit_price, post_only, **kwargs)


# Preview Functions for Limit Orders GTD
def preview_limit_order_gtd(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit order (Good Till Date)."""
    order_config = {
        "limit_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "end_time": end_time,
            "post_only": post_only
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_limit_order_gtd_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit buy order (Good Till Date)."""
    return preview_limit_order_gtd(self, product_id, "BUY", base_size, limit_price, end_time, post_only, **kwargs)


def preview_limit_order_gtd_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit sell order (Good Till Date)."""
    return preview_limit_order_gtd(self, product_id, "SELL", base_size, limit_price, end_time, post_only, **kwargs)


# Preview Functions for Limit Orders IOC
def preview_limit_order_ioc(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit order (Immediate Or Cancel)."""
    order_config = {
        "limit_limit_ioc": {
            "base_size": base_size,
            "limit_price": limit_price
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_limit_order_ioc_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit buy order (Immediate Or Cancel)."""
    return preview_limit_order_ioc(self, product_id, "BUY", base_size, limit_price, **kwargs)


def preview_limit_order_ioc_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit sell order (Immediate Or Cancel)."""
    return preview_limit_order_ioc(self, product_id, "SELL", base_size, limit_price, **kwargs)


# Preview Functions for Limit Orders FOK
def preview_limit_order_fok(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit order (Fill Or Kill)."""
    order_config = {
        "limit_limit_fok": {
            "base_size": base_size,
            "limit_price": limit_price
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_limit_order_fok_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit buy order (Fill Or Kill)."""
    return preview_limit_order_fok(self, product_id, "BUY", base_size, limit_price, **kwargs)


def preview_limit_order_fok_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a limit sell order (Fill Or Kill)."""
    return preview_limit_order_fok(self, product_id, "SELL", base_size, limit_price, **kwargs)


# Preview Functions for Stop Limit Orders GTC
def preview_stop_limit_order_gtc(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a stop limit order (Good Till Canceled)."""
    order_config = {
        "stop_limit_stop_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "stop_direction": stop_direction
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_stop_limit_order_gtc_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a stop limit buy order (Good Till Canceled)."""
    return preview_stop_limit_order_gtc(self, product_id, "BUY", base_size, limit_price, stop_price, "STOP_DIRECTION_STOP_UP", **kwargs)


def preview_stop_limit_order_gtc_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a stop limit sell order (Good Till Canceled)."""
    return preview_stop_limit_order_gtc(self, product_id, "SELL", base_size, limit_price, stop_price, "STOP_DIRECTION_STOP_DOWN", **kwargs)


# Preview Functions for Stop Limit Orders GTD
def preview_stop_limit_order_gtd(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a stop limit order (Good Till Date)."""
    order_config = {
        "stop_limit_stop_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "end_time": end_time,
            "stop_direction": stop_direction
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_stop_limit_order_gtd_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a stop limit buy order (Good Till Date)."""
    return preview_stop_limit_order_gtd(self, product_id, "BUY", base_size, limit_price, stop_price, end_time, "STOP_DIRECTION_STOP_UP", **kwargs)


def preview_stop_limit_order_gtd_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a stop limit sell order (Good Till Date)."""
    return preview_stop_limit_order_gtd(self, product_id, "SELL", base_size, limit_price, stop_price, end_time, "STOP_DIRECTION_STOP_DOWN", **kwargs)


# Preview Functions for Trigger Bracket Orders GTC
def preview_trigger_bracket_order_gtc(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a trigger bracket order (Good Till Canceled)."""
    order_config = {
        "trigger_bracket_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_trigger_bracket_order_gtc_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a trigger bracket buy order (Good Till Canceled)."""
    return preview_trigger_bracket_order_gtc(self, product_id, "BUY", base_size, limit_price, stop_trigger_price, **kwargs)


def preview_trigger_bracket_order_gtc_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a trigger bracket sell order (Good Till Canceled)."""
    return preview_trigger_bracket_order_gtc(self, product_id, "SELL", base_size, limit_price, stop_trigger_price, **kwargs)


# Preview Functions for Trigger Bracket Orders GTD
def preview_trigger_bracket_order_gtd(
    self: "RESTBase",
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a trigger bracket order (Good Till Date)."""
    order_config = {
        "trigger_bracket_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price,
            "end_time": end_time
        }
    }
    return preview_order(self, product_id, side, order_config, **kwargs)


def preview_trigger_bracket_order_gtd_buy(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a trigger bracket buy order (Good Till Date)."""
    return preview_trigger_bracket_order_gtd(self, product_id, "BUY", base_size, limit_price, stop_trigger_price, end_time, **kwargs)


def preview_trigger_bracket_order_gtd_sell(
    self: "RESTBase",
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    **kwargs
) -> Dict[str, Any]:
    """Preview a trigger bracket sell order (Good Till Date)."""
    return preview_trigger_bracket_order_gtd(self, product_id, "SELL", base_size, limit_price, stop_trigger_price, end_time, **kwargs)
