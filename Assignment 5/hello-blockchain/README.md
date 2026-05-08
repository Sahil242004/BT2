# Assignment 5 - Deploy HelloWorld Smart Contract on Ethereum Test Network

## Objective

Deploy a simple HelloWorld smart contract on Ethereum Sepolia testnet and verify deployment output.

## Project Files

- contracts/Lock.sol contains the HelloWorld contract.
- scripts/deploy.js deploys the contract and prints deployed address and message.
- hardhat.config.ts contains Sepolia network configuration.
- .env.example shows required environment variables.

## Prerequisites

- Node.js 18+
- npm
- Sepolia RPC endpoint (for example Infura or Alchemy)
- Wallet private key with test ETH on Sepolia

## Setup

1. Install dependencies

From inside `Assignment 5/hello-blockchain`:

```bash
npm install
```

From workspace root (`Blockchain _assignments`):

```bash
cd "Assignment 5/hello-blockchain"
npm install
```

2. Set environment variables

```bash
cp .env.example .env
export SEPOLIA_RPC_URL="https://sepolia.infura.io/v3/YOUR_API_KEY"
export SEPOLIA_PRIVATE_KEY="YOUR_PRIVATE_KEY_WITHOUT_0x"
```

## Compile Contract

From inside `Assignment 5/hello-blockchain`:

```bash
npm run compile
```

From workspace root (`Blockchain _assignments`):

```bash
cd "Assignment 5/hello-blockchain"
npm run compile
```

## Deploy Locally (quick check)

From inside `Assignment 5/hello-blockchain`:

```bash
npm run deploy:local
```

With custom initial message:

```bash
npx hardhat run scripts/deploy.js -- "Hello from local node"
```

## Deploy to Sepolia Testnet

From inside `Assignment 5/hello-blockchain`:

```bash
npm run deploy:sepolia
```

With custom initial message:

```bash
npx hardhat run --network sepolia scripts/deploy.js -- "Hello Sepolia"
```

## Expected Output

You should see:
- HelloWorld deployed at: <deployed_contract_address>
- Initial message: <message_you_set>

## Notes

- Keep private key secret and never commit it.
- Ensure your wallet has Sepolia ETH before deploying to testnet.
