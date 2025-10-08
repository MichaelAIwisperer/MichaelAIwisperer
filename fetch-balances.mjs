import 'dotenv/config';
import { Coinbase, Wallet } from '@coinbase/coinbase-sdk';

async function main() {
  Coinbase.configure({
    apiKeyName: process.env.COINBASE_API_KEY_NAME,
    privateKey: process.env.COINBASE_PRIVATE_KEY,
  });

  const { data: wallets } = await Wallet.listWallets({ limit: 100 });
  if (!wallets || wallets.length === 0) {
    console.log('No wallets found');
    return;
  }

  for (const w of wallets) {
    const balances = await w.listBalances();
    const lines = [];
    for (const [assetId, amount] of balances.entries()) {
      lines.push(`${assetId}:${amount.toString()}`);
    }
    console.log(`${w.getId()} [${w.getNetworkId()}]: ${lines.join(', ')}`);
  }
}

main().catch((err) => {
  console.error(err?.response?.data || err);
  process.exit(1);
});