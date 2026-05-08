import hashlib


class SimpleTokenLedger:
    def __init__(self, owner, initial_supply):
        self.balances = {owner: initial_supply}
        self.total_supply = initial_supply
        self.tx_history = []

    def balance_of(self, account):
        return self.balances.get(account, 0)

    def transfer(self, sender, receiver, amount):
        if amount <= 0:
            return False, "Rejected: amount must be greater than zero."
        if sender == receiver:
            return False, "Rejected: sender and receiver must be different."
        if self.balance_of(sender) < amount:
            return False, "Rejected: insufficient balance."

        self.balances[sender] = self.balance_of(sender) - amount
        self.balances[receiver] = self.balance_of(receiver) + amount

        tx_data = f"{sender}|{receiver}|{amount}|{len(self.tx_history)}"
        tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
        self.tx_history.append(
            {
                "hash": tx_hash,
                "from": sender,
                "to": receiver,
                "amount": amount,
            }
        )
        return True, f"Accepted: transfer recorded ({tx_hash[:12]}...)."


def print_balances(ledger, accounts):
    print("\nBalances")
    for account in accounts:
        print(f"{account}: {ledger.balance_of(account)}")


def main():
    print("Assignment 6: Token Transfer Between Accounts")

    owner = "Account_A"
    account_b = "Account_B"
    account_c = "Account_C"

    ledger = SimpleTokenLedger(owner=owner, initial_supply=1000)

    print("\nInitial state")
    print_balances(ledger, [owner, account_b, account_c])

    ok1, msg1 = ledger.transfer(owner, account_b, 150)
    print(f"\nTx1 A -> B (150): {msg1}")
    print_balances(ledger, [owner, account_b, account_c])

    ok2, msg2 = ledger.transfer(account_b, account_c, 70)
    print(f"\nTx2 B -> C (70): {msg2}")
    print_balances(ledger, [owner, account_b, account_c])

    ok3, msg3 = ledger.transfer(account_c, owner, 1000)
    print(f"\nTx3 C -> A (1000): {msg3}")
    print_balances(ledger, [owner, account_b, account_c])

    print("\nTransaction count:", len(ledger.tx_history))
    if ok1 and ok2 and not ok3:
        print("Result: token transfer logic works with balance checks.")


if __name__ == "__main__":
    main()
