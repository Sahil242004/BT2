# Assignment 6

## Problem
Write and execute a smart contract to transfer tokens between accounts.

## Files
- `SimpleToken.sol`: Solidity contract implementing basic token transfer.
- `token_transfer_demo.py`: No-dependency executable demo of transfer logic.

## Run (Primary Assignment Execution - No Dependencies)

From inside this folder:

```bash
python3 token_transfer_demo.py
```

From workspace root (`Blockchain _assignments`):

```bash
python3 "Assignment 6/token_transfer_demo.py"
```

Expected behavior:
- Initial supply assigned to Account_A.
- Valid transfers are accepted.
- Invalid transfer with insufficient balance is rejected.

## Optional: Compile `SimpleToken.sol` with Assignment 5 Hardhat

You can compile `SimpleToken.sol` using the existing Hardhat setup from Assignment 5 (no new dependency required if already installed there).

From workspace root (`Blockchain _assignments`):

```bash
cp "Assignment 6/SimpleToken.sol" "Assignment 5/hello-blockchain/contracts/SimpleToken.sol"
cd "Assignment 5/hello-blockchain"
npm run compile
```

From inside `Assignment 5/hello-blockchain`:

```bash
cp "../../Assignment 6/SimpleToken.sol" "./contracts/SimpleToken.sol"
npx hardhat compile --force
```

## Sepolia Testnet Setup and Token Transfer (Assignment 6)

This section uses the existing Hardhat project in Assignment 5 and does not add new dependencies.

From inside `Assignment 5/hello-blockchain`:

```bash
export RPC_URL="https://eth-sepolia.g.alchemy.com/v2/BVajjexJ_ZwYspLNRUnRX"
export PRIVATE_KEY="YOUR_ACTUAL_PRIVATE_KEY"
export ACCOUNT_ADDRESS="0x993c3FD3EA0d538Ef58fd2365386b046a3427485"

cp "../../Assignment 6/SimpleToken.sol" "./contracts/SimpleToken.sol"
npx hardhat compile --force
```

Deploy token on Sepolia (example initial supply = 1000000):

```bash
npm run token:deploy:sepolia
```

Copy deployed token address from output, then transfer tokens:

```bash
export TOKEN_ADDRESS="0xYourDeployedTokenAddress"
export TRANSFER_TO="0x1111111111111111111111111111111111111111"
export TRANSFER_AMOUNT="100"
npm run token:transfer:sepolia
```

Notes:
- `RPC_URL` and `PRIVATE_KEY` are supported directly in config.
- You can also use `SEPOLIA_RPC_URL` and `SEPOLIA_PRIVATE_KEY` if preferred.
- `PRIVATE_KEY` must be a real key, not placeholder text. `0x` prefix is optional.
- Keep private keys out of committed files.
