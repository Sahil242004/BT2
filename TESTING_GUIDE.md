# Testing Guide for Blockchain Assignments

This document explains how to test each assignment currently present in the codebase.

## Environment

Use Ubuntu terminal with:
- Python 3.10+
- g++
- Node.js 18+ and npm

Check versions:

```bash
python3 --version
g++ --version
node --version
npm --version
```

## Assignment 1 (Simple Blockchain + Validation + PoW)

Path:
`Assignment 1/`

### Install dependencies
No external package is required.

### Run

```bash
cd "Assignment 1"
python3 blockchain.py
```

### What to verify
- Blocks are mined with nonce updates.
- Chain prints as valid before tampering.
- After tampering, chain validation fails.
- After re-mining, chain becomes valid again.

## Assignment 2 RSA (Key Generation + Encrypt/Decrypt)

Path:
`Assignment 2 RSA/`

### Build

```bash
cd "Assignment 2 RSA"
g++ -std=c++17 rsa.cpp -o rsa
```

### Run

```bash
./rsa
```

### What to verify
- Option 1 prints public/private key pair.
- Option 2 encrypts input message value.
- Option 3 decrypts encrypted value back to original mapped value.

## Assignment 3 (Digital Wallet Basics)

Path:
`Assignment 3/`

### Install dependencies

```bash
cd "Assignment 3"
python3 -m pip install ecdsa
```

### Run

```bash
python3 crypto_wallet.py
```

### What to verify
- Two wallets are generated.
- Initial funding is added to sender wallet.
- First transaction is accepted.
- Second transaction reusing the same input is rejected.

## Assignment 4 (Transaction Simulation + Double Spending Prevention)

Path:
`Assignment 4/`

### Install dependencies

```bash
cd "Assignment 4"
python3 -m pip install ecdsa
```

### Run

```bash
python3 assignment4_double_spend.py
```

### What to verify
- Alice starts with 100 coins from genesis UTXO.
- Tx1 from Alice to Bob is accepted.
- Tx2 using same input UTXO is rejected.
- Final balances remain Alice 60, Bob 40.

## Assignment 5 (HelloWorld Smart Contract with Hardhat)

Path:
`Assignment 5/hello-blockchain/`

### Install dependencies

```bash
cd "Assignment 5/hello-blockchain"
npm install
```

### Compile

```bash
npm run compile
```

### Run tests

```bash
npm run test
```

Optional:

```bash
npx hardhat test solidity
npx hardhat test nodejs
```

### What to verify
- Contract compilation succeeds.
- Solidity and TypeScript tests pass.
- Local deployment prints deployed address and initial message.

### Deploy check (local + testnet)

```bash
npm run deploy:local
```

```bash
export SEPOLIA_RPC_URL="https://sepolia.infura.io/v3/YOUR_API_KEY"
export SEPOLIA_PRIVATE_KEY="YOUR_PRIVATE_KEY_WITHOUT_0x"
npm run deploy:sepolia
```

## Assignment 6 (Token Transfer Contract + Execution Demo)

Path:
`Assignment 6/`

### Run

```bash
cd "Assignment 6"
python3 token_transfer_demo.py
```

### What to verify
- Initial supply starts in Account_A.
- Valid transfers are accepted.
- Insufficient-balance transfer is rejected.

### Sepolia compile + deploy + transfer (tested flow)

Run from:
`Assignment 5/hello-blockchain/`

```bash
cd "Assignment 5/hello-blockchain"

export RPC_URL="https://eth-sepolia.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
export PRIVATE_KEY="YOUR_REAL_PRIVATE_KEY"
export ACCOUNT_ADDRESS="0xYourWalletAddress"

cp "../../Assignment 6/SimpleToken.sol" "./contracts/SimpleToken.sol"
npx hardhat compile --force

# deploy with default supply = 1000000
npm run token:deploy:sepolia

# after deploy, set returned token address
export TOKEN_ADDRESS="0xYourDeployedTokenAddress"
export TRANSFER_TO="0x1111111111111111111111111111111111111111"
export TRANSFER_AMOUNT="100"
npm run token:transfer:sepolia
```

Expected transfer output pattern:
- Sender before: <value>
- Receiver before: <value>
- Transfer tx hash: 0x...
- Sender after: <value>
- Receiver after: <value>

## Assignment 7 (Bitcoin Block Structure + Merkle Root)

Path:
`Assignment 7/`

### Run

```bash
cd "Assignment 7"
python3 bitcoin_merkle_analysis.py
```

### What to verify
- Sample header fields are printed.
- Merkle root is computed from sample txids.
- Simplified header hash is generated.

## Assignment 8 (Proof-of-Work Mining)

Path:
`Assignment 8/`

### Run

```bash
cd "Assignment 8"
python3 pow_mining_demo.py
```

### What to verify
- Blocks are mined with nonce search.
- Hashes satisfy the configured difficulty.
- Final chain validity is True.

## Assignment 9 (PKI-Based Identity Infrastructure Simulation)

Path:
`Assignment 9/`

### Run

```bash
cd "Assignment 9"
python3 pki_identity_demo.py
```

### What to verify
- CA key pair is created.
- Certificates are issued and accepted by registry.
- Signed message is verified using registered identity key.

## Assignment 10 (Small DApp via Python JSON-RPC)

Path:
`Assignment 10/`

### Run (offline mode)

```bash
cd "Assignment 10"
python3 dapp_contract_client.py
```

### Run (live contract call)

```bash
export ETH_RPC_URL="https://sepolia.infura.io/v3/YOUR_API_KEY"
export HELLOWORLD_CONTRACT="0xYourContractAddress"
python3 dapp_contract_client.py
```

### What to verify
- Offline mode prints setup instructions when env vars are missing.
- Live mode reads and prints `message()` from deployed contract.

## Assignment 11 (Smart Contract Search Engine)

Path:
`Assignment 11/`

### Run

```bash
cd "Assignment 11"
python3 smart_contract_search_engine.py transfer --root ".."
```

### What to verify
- Solidity files are crawled recursively.
- Query results are ranked and printed with line snippets.
- Dependency/build folders are ignored.

## Quick Full Check (all available assignments)

Run this manually section by section:

```bash
# A1
cd "Assignment 1" && python3 blockchain.py

# A2
cd "../Assignment 2 RSA" && g++ -std=c++17 rsa.cpp -o rsa && ./rsa

# A3
cd "../Assignment 3" && python3 crypto_wallet.py

# A4
cd "../Assignment 4" && python3 assignment4_double_spend.py

# A5
cd "../Assignment 5/hello-blockchain" && npm install && npm run compile && npm run test && npm run deploy:local

# A6
cd "../../Assignment 6" && python3 token_transfer_demo.py

# A7
cd "../Assignment 7" && python3 bitcoin_merkle_analysis.py

# A8
cd "../Assignment 8" && python3 pow_mining_demo.py

# A9
cd "../Assignment 9" && python3 pki_identity_demo.py

# A10
cd "../Assignment 10" && python3 dapp_contract_client.py

# A11
cd "../Assignment 11" && python3 smart_contract_search_engine.py transfer --root ".."
```
