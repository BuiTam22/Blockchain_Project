import hashlib
import json
import time
from transaction import Transaction

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions  # Danh sách giao dịch
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Tạo mã băm SHA-256 dựa trên nội dung khối"""
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.transactions, default=str)}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """Đào khối với độ khó yêu cầu"""
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []  # Giao dịch chờ xử lý

    def create_genesis_block(self):
        """Tạo khối đầu tiên (Genesis Block)"""
        return Block(0, "0", time.time(), [])

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        """Thêm giao dịch vào danh sách chờ"""
        if transaction.is_valid():
            self.pending_transactions.append(transaction)
        else:
            print("Giao dịch không hợp lệ!")

    def mine_pending_transactions(self):
        """Tạo khối mới từ danh sách giao dịch chờ"""
        if len(self.pending_transactions) == 0:
            print("Không có giao dịch nào để đào!")
            return

        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), self.pending_transactions)
        new_block.mine_block(self.difficulty)

        self.chain.append(new_block)
        self.pending_transactions = []  # Xóa giao dịch đã xử lý

    def is_chain_valid(self):
        """Kiểm tra tính toàn vẹn của Blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
