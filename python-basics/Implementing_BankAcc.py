from datetime import datetime
import json

class InsufficientFundsError(Exception):
    pass

class BankAccount():
    # A simple bank account with full transaction history
    # Had to lookup how to use the date and time module :)

    def __init__(self, owner, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative!")
        self.owner = owner
        self._balance = initial_balance     # Prefix _ -> private by convention.
        self._history = []
        self._log_transaction("OPEN", initial_balance)
    
    def _log_transaction(self, txn_type, amount):
        self._history.append({
            "type": txn_type,
            "amount": amount,
            "balance": self._balance,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def balance(self):
        # Read - only balance property.
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._log_transaction("DEPOSIT", amount)
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount:.2f}: Balance is {self._balance:.2f}")
        self._balance -= amount
        self._log_transaction("WITHDRAW", amount)
        return self._balance
    
    def transfer(self, amount, target_account):
        # Transfer Money to another bank account
        self.withdraw(amount)
        target_account.deposit(amount)
        print(f"Transferred {amount:.2f} to {target_account.owner}")

    def statement(self):
        print(f"\n{'='*50}")
        print(f"    Account Statement - {self.owner}")
        print(f"{'='*50}")
        for txn in self._history:
            sign = "+" if txn["type"] in ("DEPOSIT", "OPEN") else "-"
            print(f"    {txn['time']}   {txn['type']:<10}   {sign} {txn['amount']:>10.2f}   bal: {txn['balance']:.2f}")
        print(f"{'='*50}")
        print(f"    Current Balance : {self._balance:.2f}\n")

    def save(self, filename):
        with open("filename.txt", "w") as f:
            json.dump({"owner": self.owner, "balance": self._balance, "history": self._history}, f, indent=2)
        
    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"
    

# Demo use:
acc = BankAccount("Laksh", 10000)
acc.deposit(5000)
acc.withdraw(2500)

savings = BankAccount("Laksh Savings", 0)
acc.transfer(1500, savings)
acc.statement()
savings.statement()