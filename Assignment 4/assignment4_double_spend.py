import hashlib
import os
from dataclasses import dataclass

import ecdsa


BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def b58encode(data):
    number = int.from_bytes(data, byteorder="big")
    encoded = ""

    while number > 0:
        number, remainder = divmod(number, 58)
        encoded = BASE58_ALPHABET[remainder] + encoded

    leading_zeros = 0
    for byte in data:
        if byte == 0:
            leading_zeros += 1
        else:
            break

    if encoded == "":
        encoded = "1"

    return "1" * leading_zeros + encoded


def wallet_address_from_public_key(public_key_bytes):
    public_key_hash = hashlib.sha256(public_key_bytes).digest()
    versioned_payload = b"\x00" + public_key_hash[:20]
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
    return b58encode(versioned_payload + checksum)


def create_wallet(name):
    private_key = os.urandom(32)
    signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    public_key = b"\x04" + verifying_key.to_string()

    return {
        "name": name,
        "private_key": private_key,
        "public_key": public_key,
        "address": wallet_address_from_public_key(public_key),
        "signing_key": signing_key,
    }


@dataclass
class Transaction:
    tx_id: str
    input_utxo_id: str
    sender_address: str
    receiver_address: str
    amount: int
    signature: bytes
    sender_public_key: bytes


class UTXOLedger:
    def __init__(self):
        self.utxos = {}

    def add_utxo(self, utxo_id, owner, amount):
        self.utxos[utxo_id] = {"owner": owner, "amount": amount}

    def balance_of(self, address):
        total = 0
        for utxo in self.utxos.values():
            if utxo["owner"] == address:
                total += utxo["amount"]
        return total

    def apply_transaction(self, tx):
        input_utxo = self.utxos.get(tx.input_utxo_id)
        if input_utxo is None:
            return False, "Rejected: input UTXO not found (already spent or invalid)."

        if input_utxo["owner"] != tx.sender_address:
            return False, "Rejected: sender does not own this UTXO."

        if tx.amount <= 0:
            return False, "Rejected: amount must be greater than zero."

        if tx.amount > input_utxo["amount"]:
            return False, "Rejected: insufficient amount in input UTXO."

        sign_message = f"{tx.input_utxo_id}|{tx.sender_address}|{tx.receiver_address}|{tx.amount}".encode()
        digest = hashlib.sha256(sign_message).digest()

        try:
            verifying_key = ecdsa.VerifyingKey.from_string(tx.sender_public_key[1:], curve=ecdsa.SECP256k1)
            if not verifying_key.verify(tx.signature, digest):
                return False, "Rejected: signature verification failed."
        except Exception:
            return False, "Rejected: invalid signature payload."

        del self.utxos[tx.input_utxo_id]

        receiver_output = f"{tx.tx_id}:0"
        self.add_utxo(receiver_output, tx.receiver_address, tx.amount)

        change = input_utxo["amount"] - tx.amount
        if change > 0:
            change_output = f"{tx.tx_id}:1"
            self.add_utxo(change_output, tx.sender_address, change)

        return True, "Accepted: transaction committed."


def create_signed_transaction(wallet, input_utxo_id, to_address, amount):
    sign_message = f"{input_utxo_id}|{wallet['address']}|{to_address}|{amount}".encode()
    digest = hashlib.sha256(sign_message).digest()
    signature = wallet["signing_key"].sign(digest)
    tx_id = hashlib.sha256(signature + digest).hexdigest()[:20]

    return Transaction(
        tx_id=tx_id,
        input_utxo_id=input_utxo_id,
        sender_address=wallet["address"],
        receiver_address=to_address,
        amount=amount,
        signature=signature,
        sender_public_key=wallet["public_key"],
    )


def print_wallet(wallet):
    print(f"\n{wallet['name']} Wallet")
    print(f"Private Key : {wallet['private_key'].hex()}")
    print(f"Public Key  : {wallet['public_key'].hex()}")
    print(f"Address     : {wallet['address']}")


def print_balances(ledger, wallet_a, wallet_b):
    print("\nBalances")
    print(f"{wallet_a['name']}: {ledger.balance_of(wallet_a['address'])}")
    print(f"{wallet_b['name']}: {ledger.balance_of(wallet_b['address'])}")


def main():
    print("Assignment 4: Transaction Simulation and Double-Spending Prevention")

    alice = create_wallet("Alice")
    bob = create_wallet("Bob")

    print_wallet(alice)
    print_wallet(bob)

    ledger = UTXOLedger()

    genesis_utxo_id = "genesis:0"
    ledger.add_utxo(genesis_utxo_id, alice["address"], 100)
    print("\nGenesis funding: Alice receives 100 coins")
    print_balances(ledger, alice, bob)

    tx1 = create_signed_transaction(alice, genesis_utxo_id, bob["address"], 40)
    ok1, message1 = ledger.apply_transaction(tx1)
    print(f"\nTx1 (Alice -> Bob, 40): {message1}")
    print_balances(ledger, alice, bob)

    tx2 = create_signed_transaction(alice, genesis_utxo_id, bob["address"], 20)
    ok2, message2 = ledger.apply_transaction(tx2)
    print(f"\nTx2 (double-spend attempt with same input): {message2}")
    print_balances(ledger, alice, bob)

    if ok1 and not ok2:
        print("\nResult: Double spending prevented successfully.")


if __name__ == "__main__":
    main()
