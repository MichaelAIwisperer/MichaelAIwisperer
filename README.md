- 👋 Hi, I’m @MichaelAIwisperer
- 👀 I’m interested in AI, machine learning, prompt engineering, ethical AI development and coding applications that improve the quality of life ...
- 🌱 I’m currently learning to prompt, studying other developers work like siraj raval
- 💞️ I’m looking to collaborate on apps
- 📫 How to reach me facebook, linkedin

<!---
MichaelAIwisperer/MichaelAIwisperer is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

## Coinbase Advanced Python SDK setup

### Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If `venv` is missing:

```bash
sudo apt-get update && sudo apt-get install -y python3-venv
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the public example

```bash
python coinbase_example.py
```

The example fetches server time, a list of products, best bid/ask, a small order book snapshot, recent trades, and recent 1‑minute candles. All public; no credentials needed.

### Optional: authenticated calls

Set environment variables to enable authenticated endpoints (e.g. list accounts):

```bash
export COINBASE_API_KEY=your_key
export COINBASE_API_SECRET=your_secret
python coinbase_example.py
```

Make sure your API key has the correct permissions for the endpoints you call.

