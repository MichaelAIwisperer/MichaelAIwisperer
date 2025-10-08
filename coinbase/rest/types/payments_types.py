"""Payment method type definitions for Coinbase API"""

from typing import Any, Dict, List, Optional


class ListPaymentMethodsResponse:
    """Response type for listing payment methods"""
    
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.payment_methods = data.get("payment_methods", [])
    
    def __repr__(self) -> str:
        return f"ListPaymentMethodsResponse(payment_methods={len(self.payment_methods)})"


class GetPaymentMethodResponse:
    """Response type for getting a single payment method"""
    
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.payment_method = data.get("payment_method", {})
    
    def __repr__(self) -> str:
        return f"GetPaymentMethodResponse(payment_method={self.payment_method.get('id', 'unknown')})"
