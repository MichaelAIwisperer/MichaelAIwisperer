"""
Configuration management for Coinbase Trader
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for Coinbase trading bot"""
    
    # Coinbase API credentials
    API_KEY = os.getenv('COINBASE_API_KEY')
    API_SECRET = os.getenv('COINBASE_API_SECRET')
    
    # Trading settings
    DEFAULT_PRODUCT_ID = os.getenv('DEFAULT_PRODUCT_ID', 'BTC-USD')
    TRADE_AMOUNT_USD = float(os.getenv('TRADE_AMOUNT_USD', '10.00'))
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        if not cls.API_KEY or cls.API_KEY == 'your_api_key_here':
            raise ValueError("COINBASE_API_KEY not set in .env file")
        if not cls.API_SECRET or cls.API_SECRET == 'your_api_secret_here':
            raise ValueError("COINBASE_API_SECRET not set in .env file")
        return True
