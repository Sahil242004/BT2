# Blockchain Assignments – Theory, Explanation & Flow

## Assignment 1 – Basic Blockchain Implementation
### Theory
A blockchain is a chain of blocks where each block stores data, timestamp, previous block hash, and its own hash. Hashing ensures integrity because even a tiny change in data changes the entire hash.

### What This Assignment Does
- Creates blocks using Python.
- Links blocks through previous hashes.
- Validates chain integrity.
- Implements basic Proof-of-Work (PoW).

### Flow
1. Create Genesis Block.
2. Add transaction/data to new block.
3. Generate hash using SHA-256.
4. Link new block with previous block hash.
5. Mine block using nonce + difficulty.
6. Verify chain validity.

### Core Concepts
- SHA-256 Hashing
- Immutable Ledger
- Linked Data Structure
- Proof-of-Work

---

## Assignment 2 – RSA Encryption
### Theory
RSA is an asymmetric cryptography algorithm using:
- Public Key → Encryption
- Private Key → Decryption

Security depends on the difficulty of factoring large prime numbers.

### What This Assignment Does
- Generates RSA keys.
- Encrypts plaintext.
- Decrypts ciphertext.
- Demonstrates secure communication.

### Flow
1. Select two prime numbers.
2. Compute n = p × q.
3. Compute Euler Totient φ(n).
4. Generate public/private keys.
5. Encrypt message using public key.
6. Decrypt using private key.

### Core Concepts
- Public Key Cryptography
- Prime Factorization
- Modular Arithmetic
- Encryption & Decryption

---

## Assignment 3 – Crypto Wallet Simulation
### Theory
A crypto wallet stores cryptographic keys, not actual coins. Wallets use public-private key pairs for identity and transaction authorization.

### What This Assignment Does
- Generates wallet keys.
- Simulates digital wallet behavior.
- Uses ECDSA signatures.

### Flow
1. Generate private key.
2. Derive public key.
3. Create wallet address.
4. Sign messages/transactions.
5. Verify signatures.

### Core Concepts
- Digital Signatures
- ECDSA
- Wallet Address Generation
- Authentication

---

## Assignment 4 – Double Spending Prevention
### Theory
Double spending means attempting to spend the same digital asset more than once. Blockchain prevents this using transaction validation and ledger tracking.

### What This Assignment Does
- Simulates wallet transactions.
- Detects duplicate spending attempts.
- Validates balances before transfer.

### Flow
1. Create sender and receiver wallets.
2. Initiate transaction.
3. Check sender balance.
4. Verify transaction uniqueness.
5. Approve or reject transaction.

### Core Concepts
- Transaction Validation
- Ledger Consistency
- UTXO/Balance Tracking
- Fraud Prevention

---

## Assignment 5 – Smart Contract Deployment on Ethereum
### Theory
A smart contract is self-executing code deployed on blockchain networks like Ethereum. Once deployed, it becomes immutable and decentralized.

### What This Assignment Does
- Uses Solidity smart contracts.
- Deploys contract on Sepolia testnet.
- Uses Hardhat framework.

### Flow
1. Write Solidity contract.
2. Compile contract.
3. Configure Hardhat.
4. Connect wallet + Sepolia RPC.
5. Deploy contract.
6. Receive deployed contract address.

### Core Concepts
- Ethereum
- Solidity
- Gas Fees
- Hardhat
- Smart Contract Deployment

---

## Assignment 6 – Token Transfer Smart Contract
### Theory
Blockchain tokens represent digital assets. Smart contracts manage balances and transfer logic securely.

### What This Assignment Does
- Implements token transfer logic.
- Simulates account balances.
- Validates sufficient funds.

### Flow
1. Initialize token supply.
2. Assign balance to owner.
3. Request token transfer.
4. Verify balance.
5. Update sender and receiver balances.
6. Reject invalid transfers.

### Core Concepts
- ERC-style Tokens
- Balance Management
- Transaction Execution
- Smart Contract Logic

---

## Assignment 7 – Bitcoin Block & Merkle Root Analysis
### Theory
Bitcoin stores transactions inside blocks. Merkle Trees are used to efficiently verify transactions using hashes.

### What This Assignment Does
- Analyzes Bitcoin block structure.
- Computes Merkle Root.
- Demonstrates double SHA-256 hashing.

### Flow
1. Collect transaction hashes.
2. Pair adjacent hashes.
3. Apply double SHA-256.
4. Repeat until single root hash remains.
5. Use root inside block header.

### Core Concepts
- Bitcoin Block Structure
- Merkle Tree
- Transaction Verification
- Double SHA-256

---

## Assignment 8 – Proof-of-Work Mining
### Theory
Proof-of-Work is a consensus mechanism where miners solve computational puzzles to validate blocks.

### What This Assignment Does
- Mines blocks using nonce values.
- Searches for hash meeting difficulty condition.
- Measures mining effort.

### Flow
1. Create block.
2. Start nonce from 0.
3. Generate block hash.
4. Check difficulty condition.
5. If invalid → increment nonce.
6. If valid → block mined.

### Core Concepts
- Consensus Mechanism
- Mining
- Nonce
- Difficulty Target
- Hash Puzzle

---

## Assignment 9 – PKI-Based Identity System
### Theory
PKI (Public Key Infrastructure) manages digital identities using certificates issued by trusted Certificate Authorities (CA).

### What This Assignment Does
- Simulates Certificate Authority.
- Issues certificates.
- Verifies identities.
- Signs and verifies messages.

### Flow
1. Generate user key pair.
2. CA issues certificate.
3. Store certificate in registry.
4. User signs message.
5. Verify signature using certificate.

### Core Concepts
- PKI
- Digital Certificates
- Certificate Authority
- Identity Verification
- Authentication

---

## Assignment 10 – DApp Contract Interaction
### Theory
A DApp (Decentralized Application) interacts with blockchain smart contracts using APIs and JSON-RPC communication.

### What This Assignment Does
- Connects Python client to Ethereum node.
- Calls deployed contract functions.
- Uses JSON-RPC requests.

### Flow
1. Connect to Ethereum RPC endpoint.
2. Load contract address.
3. Build eth_call request.
4. Send request to blockchain.
5. Receive encoded response.
6. Decode returned data.

### Core Concepts
- DApp Architecture
- JSON-RPC
- Ethereum API
- Contract Interaction
- ABI Decoding

---

## Assignment 11 – Smart Contract Search Engine
### Theory
Smart contract analysis tools help developers search and inspect Solidity code efficiently.

### What This Assignment Does
- Crawls Solidity files.
- Supports keyword and regex search.
- Ranks matching contracts.

### Flow
1. Traverse project folders.
2. Detect .sol files.
3. Read contract source code.
4. Search keyword/regex.
5. Rank results by occurrences.
6. Display matching lines.

### Core Concepts
- Solidity Parsing
- Code Search
- Regex Matching
- Static Analysis

---

# Overall Learning Outcome
These assignments collectively cover the core pillars of blockchain technology:
- Blockchain Fundamentals
- Cryptography
- Wallets & Transactions
- Smart Contracts
- Ethereum Development
- Mining & Consensus
- Identity Management
- DApp Interaction
- Blockchain Analysis Tools

It starts from the raw stone age of blockchain — hashes and chains — and slowly climbs toward decentralized applications and infrastructure. Like watching civilization evolve in fast-forward, but with more SHA-256 and fewer dragons.

