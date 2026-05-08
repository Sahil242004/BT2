import hashlib
import os
from dataclasses import dataclass

import ecdsa

try:
	from Cryptodome.Hash import RIPEMD160 as CryptoRIPEMD160
except Exception:
	CryptoRIPEMD160 = None


BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def b58encode(data):
	num = int.from_bytes(data, byteorder="big")
	encoded = ""
	while num > 0:
		num, rem = divmod(num, 58)
		encoded = BASE58_ALPHABET[rem] + encoded

	leading_zero_count = 0
	for byte in data:
		if byte == 0:
			leading_zero_count += 1
		else:
			break

	return "1" * leading_zero_count + (encoded or "1")


def ripemd160_digest(data):
	try:
		h = hashlib.new("ripemd160")
		h.update(data)
		return h.digest()
	except ValueError:
		if CryptoRIPEMD160 is None:
			raise RuntimeError("RIPEMD160 is unavailable. Install pycryptodome or use a Python build with ripemd160.")
		h = CryptoRIPEMD160.new()
		h.update(data)
		return h.digest()


def generate_wallet():
	private_key = os.urandom(32)
	signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
	verifying_key = signing_key.get_verifying_key()
	public_key = b"\x04" + verifying_key.to_string()

	sha256_hash = hashlib.sha256(public_key).digest()
	ripemd160 = ripemd160_digest(sha256_hash)
	network_byte = b"\x00" + ripemd160
	checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]
	address = b58encode(network_byte + checksum)

	return {
		"private_key": private_key,
		"public_key": public_key,
		"address": address,
		"signing_key": signing_key,
		"verifying_key": verifying_key,
	}


@dataclass
class Transaction:
	tx_id: str
	input_utxo_id: str
	from_address: str
	to_address: str
	amount: int
	signature: bytes
	sender_public_key: bytes


class SimpleUTXOLedger:
	def __init__(self):
		self.utxos = {}

	def add_utxo(self, utxo_id, owner, amount):
		self.utxos[utxo_id] = {"owner": owner, "amount": amount}

	def show_balances(self):
		balances = {}
		for _, utxo in self.utxos.items():
			balances[utxo["owner"]] = balances.get(utxo["owner"], 0) + utxo["amount"]
		return balances

	def apply_transaction(self, tx):
		input_utxo = self.utxos.get(tx.input_utxo_id)

		if input_utxo is None:
			return False, "Rejected: input UTXO does not exist (already spent or invalid)."

		if input_utxo["owner"] != tx.from_address:
			return False, "Rejected: input UTXO is not owned by sender."

		if tx.amount <= 0:
			return False, "Rejected: amount must be positive."

		if tx.amount > input_utxo["amount"]:
			return False, "Rejected: insufficient UTXO balance."

		message = f"{tx.input_utxo_id}|{tx.from_address}|{tx.to_address}|{tx.amount}".encode()
		tx_hash = hashlib.sha256(message).digest()

		try:
			vk = ecdsa.VerifyingKey.from_string(tx.sender_public_key[1:], curve=ecdsa.SECP256k1)
			if not vk.verify(tx.signature, tx_hash):
				return False, "Rejected: invalid signature."
		except Exception:
			return False, "Rejected: signature verification failed."

		# Spend the input and create outputs.
		del self.utxos[tx.input_utxo_id]

		receiver_utxo_id = f"{tx.tx_id}:0"
		self.add_utxo(receiver_utxo_id, tx.to_address, tx.amount)

		change = input_utxo["amount"] - tx.amount
		if change > 0:
			change_utxo_id = f"{tx.tx_id}:1"
			self.add_utxo(change_utxo_id, tx.from_address, change)

		return True, "Accepted: transaction added to ledger."


def create_signed_transaction(signing_key, sender_public_key, input_utxo_id, from_addr, to_addr, amount):
	message = f"{input_utxo_id}|{from_addr}|{to_addr}|{amount}".encode()
	tx_hash = hashlib.sha256(message).digest()
	signature = signing_key.sign(tx_hash)
	tx_id = hashlib.sha256(signature + tx_hash).hexdigest()[:16]

	return Transaction(
		tx_id=tx_id,
		input_utxo_id=input_utxo_id,
		from_address=from_addr,
		to_address=to_addr,
		amount=amount,
		signature=signature,
		sender_public_key=sender_public_key,
	)


def print_wallet(name, wallet):
	print(f"\n{name} Wallet")
	print(f"Private Key: {wallet['private_key'].hex()}")
	print(f"Public Key : {wallet['public_key'].hex()}")
	print(f"Address    : {wallet['address']}")


def print_balances(ledger, alice_addr, bob_addr):
	balances = ledger.show_balances()
	print("\nCurrent Balances")
	print(f"Alice: {balances.get(alice_addr, 0)}")
	print(f"Bob  : {balances.get(bob_addr, 0)}")


if __name__ == "__main__":
	print("Step 1-3: Generate two wallets")
	alice = generate_wallet()
	bob = generate_wallet()

	print_wallet("Alice", alice)
	print_wallet("Bob", bob)

	print("\nStep 4: Simulate transaction + double-spending prevention")
	ledger = SimpleUTXOLedger()

	genesis_utxo_id = "genesis:0"
	ledger.add_utxo(genesis_utxo_id, alice["address"], 100)
	print("Genesis funding: Alice receives 100 coins")
	print_balances(ledger, alice["address"], bob["address"])

	tx1 = create_signed_transaction(
		signing_key=alice["signing_key"],
		sender_public_key=alice["public_key"],
		input_utxo_id=genesis_utxo_id,
		from_addr=alice["address"],
		to_addr=bob["address"],
		amount=40,
	)
	ok, msg = ledger.apply_transaction(tx1)
	print(f"\nTx1 (Alice -> Bob, 40): {msg}")
	print_balances(ledger, alice["address"], bob["address"])

	tx2 = create_signed_transaction(
		signing_key=alice["signing_key"],
		sender_public_key=alice["public_key"],
		input_utxo_id=genesis_utxo_id,
		from_addr=alice["address"],
		to_addr=bob["address"],
		amount=30,
	)
	ok2, msg2 = ledger.apply_transaction(tx2)
	print(f"\nTx2 Reusing same input (double-spend attempt): {msg2}")
	print_balances(ledger, alice["address"], bob["address"])

	if not ok2:
		print("\nResult: Double spending successfully prevented.")
