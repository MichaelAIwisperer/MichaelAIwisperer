import 'dotenv/config';
import { Coinbase } from '@coinbase/coinbase-sdk';

async function main() {
  console.log('SDK keys present:', Boolean(process.env.COINBASE_API_KEY_NAME && process.env.COINBASE_PRIVATE_KEY));
  const cb = Coinbase.configure({
    apiKeyName: process.env.COINBASE_API_KEY_NAME,
    privateKey: process.env.COINBASE_PRIVATE_KEY,
  });
  console.log('Coinbase configured:', Boolean(cb));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});