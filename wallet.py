import hashlib
import random
from transaction import Transaction


class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 1000  # Mặc định có 1000 coin
        self.private_key, self.public_key = self.generate_keys()

    def generate_keys(self):
        """Tạo khóa giả lập"""
        private_key = hashlib.sha256(str(random.randint(0, int(1e6))).encode()).hexdigest()
        public_key = hashlib.sha256(private_key.encode()).hexdigest()
        return private_key, public_key

    def send_money(self, receiver, amount):
        """Tạo giao dịch mới"""
        if amount > self.balance:
            print("Không đủ số dư!")
            return None
        self.balance -= amount
        return Transaction(self.public_key, receiver, amount)

    def __repr__(self):
        return f"Wallet({self.owner}, Balance: {self.balance})"
