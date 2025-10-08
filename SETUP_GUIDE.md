# Coinbase Trading Bot - Setup Guide

A Python-based trading bot for Coinbase Advanced Trade API with an interactive CLI interface.

## Features

- 📊 View portfolio balances
- 💰 Real-time price monitoring
- 🛒 Market buy/sell orders
- 📈 Limit buy/sell orders
- 📋 Order management
- 🔄 Multiple trading pairs support
- ✅ Built-in error handling

---

## Prerequisites

- Python 3.7 or higher
- Coinbase account with API access
- Basic understanding of cryptocurrency trading

---

## Installation

### 1. Clone or Download This Repository

```bash
cd /workspace
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install coinbase-advanced-py python-dotenv requests
```

### 3. Get Coinbase API Credentials

1. Log into your [Coinbase account](https://www.coinbase.com/)
2. Go to **Settings** → **API**
3. Click **New API Key**
4. Set permissions:
   - ✅ **View** (to see balances and prices)
   - ✅ **Trade** (to place orders)
   - ⚠️ Only enable what you need for security
5. Save your **API Key** and **API Secret** securely

⚠️ **IMPORTANT**: Never share your API keys or commit them to version control!

### 4. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your credentials:
   ```bash
   nano .env
   # or use any text editor
   ```

3. Replace the placeholder values:
   ```
   COINBASE_API_KEY=your_actual_api_key_here
   COINBASE_API_SECRET=your_actual_api_secret_here
   DEFAULT_PRODUCT_ID=BTC-USD
   TRADE_AMOUNT_USD=10.00
   ```

---

## Usage

### Start the Trading Bot

```bash
python main.py
```

### Interactive Menu

Once started, you'll see a menu with these options:

```
1.  View Portfolio           - See all your account balances
2.  View Current Price       - Check current price for any trading pair
3.  View Product Info        - Get detailed info about a trading pair
4.  Market Buy              - Buy at current market price
5.  Market Sell             - Sell at current market price
6.  Limit Buy               - Place a buy order at specific price
7.  Limit Sell              - Place a sell order at specific price
8.  View Orders             - See all your open/past orders
9.  Cancel Orders           - Cancel specific orders by ID
10. Change Product          - Switch default trading pair
0.  Exit                    - Close the bot
```

### Example Workflow

1. **Check your portfolio**: Option 1
2. **View current BTC price**: Option 2
3. **Buy $10 worth of BTC**: Option 4
   - Enter product ID: `BTC-USD` (or press Enter for default)
   - Enter amount: `10`
   - Confirm: `yes`
4. **View your orders**: Option 8

---

## Available Trading Pairs

Common pairs (check Coinbase for full list):
- `BTC-USD` - Bitcoin to US Dollar
- `ETH-USD` - Ethereum to US Dollar
- `SOL-USD` - Solana to US Dollar
- `DOGE-USD` - Dogecoin to US Dollar
- `ADA-USD` - Cardano to US Dollar
- `MATIC-USD` - Polygon to US Dollar

---

## Project Structure

```
/workspace/
│
├── main.py                 # Entry point with CLI interface
├── coinbase_trader.py      # Main trading logic and API calls
├── config.py              # Configuration management
├── requirements.txt        # Python dependencies
├── .env                   # Your API credentials (DO NOT COMMIT)
├── .env.example           # Template for .env file
├── .gitignore             # Protects sensitive files
└── SETUP_GUIDE.md         # This file
```

---

## Safety Tips

### 🚨 Important Security Practices

1. **Start Small**: Test with small amounts first ($5-10)
2. **Use API Restrictions**: Limit API key permissions in Coinbase settings
3. **Enable 2FA**: Use two-factor authentication on your Coinbase account
4. **Never Share Keys**: Keep your `.env` file private
5. **Monitor Your Account**: Regularly check your Coinbase account for unexpected activity

### 💡 Trading Tips

1. **Understand Market vs Limit Orders**:
   - **Market orders** execute immediately at current price
   - **Limit orders** execute only when price reaches your target

2. **Be Aware of Fees**: Coinbase charges trading fees on each transaction

3. **Don't Invest More Than You Can Afford to Lose**: Cryptocurrency is volatile

---

## Troubleshooting

### "Failed to initialize trader"

**Solution**: 
- Check that `.env` file exists and has valid credentials
- Verify API key has correct permissions
- Ensure you've run `pip install -r requirements.txt`

### "Error fetching accounts"

**Solution**:
- Verify your API credentials are correct
- Check your internet connection
- Ensure API key hasn't been revoked in Coinbase settings

### "Invalid product ID"

**Solution**:
- Use format like `BTC-USD`, `ETH-USD` (always UPPERCASE)
- Verify the pair exists on Coinbase Advanced Trade
- Check [Coinbase product list](https://www.coinbase.com/advanced-trade)

### "Insufficient funds"

**Solution**:
- Check your account balance (Option 1 in menu)
- Ensure you have enough USD or crypto for the trade
- Account for trading fees

---

## Advanced Usage

### Using the Trader Class Programmatically

You can also use the `CoinbaseTrader` class in your own Python scripts:

```python
from coinbase_trader import CoinbaseTrader

# Initialize trader
trader = CoinbaseTrader()

# Get current BTC price
price = trader.get_current_price('BTC-USD')
print(f"BTC Price: ${price}")

# View portfolio
trader.display_portfolio()

# Place a market buy order
trader.market_buy('BTC-USD', 10.00)  # Buy $10 of BTC
```

### Automating Trades

Create a custom script for automated trading:

```python
from coinbase_trader import CoinbaseTrader
import time

trader = CoinbaseTrader()

# Example: Buy if price drops below threshold
target_price = 30000
current_price = trader.get_current_price('BTC-USD')

if current_price < target_price:
    trader.market_buy('BTC-USD', 100)
    print(f"Bought BTC at ${current_price}")
```

⚠️ **Warning**: Automated trading carries significant risk. Test thoroughly with small amounts!

---

## Testing in Terminal

You can test individual components:

```bash
# Test connection
python -c "from coinbase_trader import CoinbaseTrader; t = CoinbaseTrader(); print('Connected!')"

# Get BTC price
python -c "from coinbase_trader import CoinbaseTrader; t = CoinbaseTrader(); print(t.get_current_price('BTC-USD'))"

# View portfolio
python -c "from coinbase_trader import CoinbaseTrader; t = CoinbaseTrader(); t.display_portfolio()"
```

---

## Resources

- [Coinbase Advanced Trade API Documentation](https://docs.cloud.coinbase.com/advanced-trade-api/docs)
- [Coinbase SDK Python GitHub](https://github.com/coinbase/coinbase-advanced-py)
- [Cryptocurrency Trading Basics](https://www.coinbase.com/learn)

---

## Disclaimer

This software is for educational purposes only. Use at your own risk. The developers are not responsible for any financial losses incurred through the use of this bot. Cryptocurrency trading carries substantial risk.

**Always do your own research and never invest more than you can afford to lose.**

---

## Support

If you encounter issues:
1. Check this guide's Troubleshooting section
2. Review your API key permissions
3. Ensure all dependencies are installed
4. Check Coinbase API status: https://status.coinbase.com/

---

## License

This project is open source and available for educational purposes.

---

**Happy Trading! 🚀**

Remember: Start small, learn continuously, and trade responsibly.
