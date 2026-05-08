# Blockchain Assignments Workspace

This repository contains assignment-wise implementations.

## Run Each Assignment Individually

### Assignment 1

```bash
cd "Assignment 1"
python3 blockchain.py
```

### Assignment 2 RSA

```bash
cd "Assignment 2 RSA"
g++ -std=c++17 rsa.cpp -o rsa
./rsa
```

### Assignment 3

```bash
cd "Assignment 3"
python3 crypto_wallet.py
```

### Assignment 4

```bash
cd "Assignment 4"
python3 assignment4_double_spend.py
```

### Assignment 5 (HelloWorld Smart Contract)

```bash
cd "Assignment 5/hello-blockchain"
npm install
npm run compile
npm run test
npm run deploy:local
```

### Assignment 6

```bash
cd "Assignment 6"
python3 token_transfer_demo.py
```

### Assignment 7

```bash
cd "Assignment 7"
python3 bitcoin_merkle_analysis.py
```

### Assignment 8

```bash
cd "Assignment 8"
python3 pow_mining_demo.py
```

### Assignment 9

```bash
cd "Assignment 9"
python3 pki_identity_demo.py
```

### Assignment 10

```bash
cd "Assignment 10"
python3 dapp_contract_client.py
```

Optional testnet call:

```bash
export ETH_RPC_URL="https://sepolia.infura.io/v3/YOUR_API_KEY"
export HELLOWORLD_CONTRACT="0xYourContractAddress"
python3 dapp_contract_client.py
```

### Assignment 11

```bash
cd "Assignment 11"
python3 smart_contract_search_engine.py transfer --root ".."
```

Optional Solidity compile path for Assignment 6 using existing Hardhat project:

```bash
cp "Assignment 6/SimpleToken.sol" "Assignment 5/hello-blockchain/contracts/SimpleToken.sol"
cd "Assignment 5/hello-blockchain"
npm run compile
```

## Full Testing Document

See:
- TESTING_GUIDE.md
