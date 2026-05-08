# Assignment 10

## Problem
Build a small DApp: interact with deployed smart contract using Python API.

## What This Implementation Includes
- Minimal JSON-RPC client in Python (no external package).
- Calls `message()` on deployed HelloWorld contract using `eth_call`.
- ABI decoding for dynamic string return values.

## Run (Offline Demo)

From inside this folder:

```bash
python3 dapp_contract_client.py
```

From workspace root (`Blockchain _assignments`):

```bash
python3 "Assignment 10/dapp_contract_client.py"
```

## Run Against Testnet Contract

From inside this folder:

```bash
export ETH_RPC_URL="https://sepolia.infura.io/v3/YOUR_API_KEY"
export HELLOWORLD_CONTRACT="0xYourContractAddress"
python3 dapp_contract_client.py
```

From workspace root (`Blockchain _assignments`):

```bash
export ETH_RPC_URL="https://sepolia.infura.io/v3/YOUR_API_KEY"
export HELLOWORLD_CONTRACT="0xYourContractAddress"
python3 "Assignment 10/dapp_contract_client.py"
```

## Dependencies
No extra dependencies required.
