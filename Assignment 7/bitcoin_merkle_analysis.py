import hashlib
import json


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def double_sha256_hex(hex_string):
    raw = bytes.fromhex(hex_string)
    first = hashlib.sha256(raw).digest()
    second = hashlib.sha256(first).digest()
    return second.hex()


def merkle_root(txids):
    if not txids:
        return None

    layer = txids[:]
    while len(layer) > 1:
        if len(layer) % 2 == 1:
            layer.append(layer[-1])

        next_layer = []
        for i in range(0, len(layer), 2):
            combined = layer[i] + layer[i + 1]
            next_layer.append(double_sha256_hex(combined))
        layer = next_layer

    return layer[0]


def sample_block():
    return {
        "version": 2,
        "previous_block_hash": "0000000000000000000769c4fcb89f4b20f4f6f5282af6f44f3ccf4ecf5821bd",
        "timestamp": 1711978200,
        "bits": "17034219",
        "nonce": 103134495,
        "transactions": [
            "a3f1f7f0fdf7bc6b63d4f01d8f0b61ed2a2f2f2eb1b52ef9dbf6b4e9a281b6a1",
            "5bb05f3b8f37e1a7fb1ea80b2df4ca3469eb6a61df77d2d07f8af0bde7f726dc",
            "8d52e5b8d3b6adbc3f4eac35a6b98a10e27d7f3b13f6b60b4f2d2e4f3ed7d9d5",
            "ec4a2f36e689fb8f58f7c1ed7d88ee5f74290f5f83f7adf36e9f1cb685fd2f8a",
            "03f89abc0e72a4e3f5d9038a6d2c4f9d2f4f7eead9899d3bb31811cf8a2bd22b",
        ],
    }


def main():
    block = sample_block()

    print("Assignment 7: Bitcoin Block Structure + Merkle Root")
    print("\nHeader Fields")
    print(json.dumps({
        "version": block["version"],
        "previous_block_hash": block["previous_block_hash"],
        "timestamp": block["timestamp"],
        "bits": block["bits"],
        "nonce": block["nonce"],
        "transaction_count": len(block["transactions"]),
    }, indent=2))

    print("\nSample Transaction IDs")
    for i, txid in enumerate(block["transactions"], start=1):
        print(f"{i}. {txid}")

    root = merkle_root(block["transactions"])
    print("\nComputed Merkle Root")
    print(root)

    header_data = (
        f"{block['version']}|{block['previous_block_hash']}|{root}|"
        f"{block['timestamp']}|{block['bits']}|{block['nonce']}"
    ).encode()
    block_header_hash = sha256_hex(header_data)

    print("\nSimplified Header Hash (single SHA-256 over formatted header fields)")
    print(block_header_hash)


if __name__ == "__main__":
    main()
