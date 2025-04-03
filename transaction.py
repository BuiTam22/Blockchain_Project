import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.tx_hash = self.calculate_hash()

    def calculate_hash(self):
        """Tạo mã băm giao dịch"""
        tx_string = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return hashlib.sha256(tx_string.encode()).hexdigest()

    def is_valid(self):
        """Kiểm tra tính hợp lệ của giao dịch"""
        if self.amount <= 0:
            return False
        return True

    def __repr__(self):
        return f"Tx({self.sender} -> {self.receiver}, {self.amount})"
