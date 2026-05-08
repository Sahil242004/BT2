# Assignment 11

## Problem
Develop a smart contract search engine.

## What This Implementation Includes
- Crawls Solidity files (`.sol`) recursively.
- Supports plain text and regex search.
- Returns ranked results by number of matches.
- Prints top matching lines for quick inspection.

## Run

From inside this folder:

```bash
python3 smart_contract_search_engine.py transfer --root ".."
```

From workspace root (`Blockchain _assignments`):

```bash
python3 "Assignment 11/smart_contract_search_engine.py" transfer --root "."
```

Regex example:

```bash
python3 smart_contract_search_engine.py "function\\s+setMessage" --root ".." --regex
```

## Dependencies
No extra dependencies required.
